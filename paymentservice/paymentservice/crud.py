from paymentservice.models import payment
from sqlmodel import Session, select
from typing import List
from paymentservice.schemas import PaymentCreate

def creatPayment(db: Session, payment:PaymentCreate)-> payment:
    dbPayment = payment(**payment.dict())
    db.add(dbPayment)
    db.commit()
    db.refresh(dbPayment)
    return dbPayment


def getPayment(db:Session, skip: int = 0, limit = 100)-> List[payment]:
    return db.exce(select(payment).offset(skip).limit(limit)).all()

def getPayment_id(db: Session, payment_id: int) -> payment:
    return db.get(payment, payment_id)

def updatePayment(db: Session, payment_id: int, payment: PaymentCreate) -> payment:
    dbPayment = db.get(payment, payment_id)
    if dbPayment is None:
        return None
    for key, value in payment.dict(exclude_unset=True).items():
        setattr(dbPayment, key, value)
    db.add(dbPayment)
    db.commit()
    db.refresh(dbPayment)
    return dbPayment

def deletePayment(db: Session, payment_id: int) -> payment:
    dbPayment = db.get(payment, payment_id)
    if dbPayment is None:
        return None
    db.delete(dbPayment)
    db.commit()
    return dbPayment

def updatedPayment(db: Session, order_id: int, status: str):
    statment = select(payment).where(payment.order_id == order_id)
    results = db.exec(statment)
    payment = results.one_or_none()
    if payment:
        payment.status = status
        db.add(payment)
        db.commit()
        db.refresh(payment)
    return payment

    

