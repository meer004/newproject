from sqlmodel import Session
from notificationservice.models import Notification
from notificationservice.schemas import NotificationCreate






def create_notification(notification: NotificationCreate, session: Session):
    db_notification = Notification(**notification.dict())
    session.add(db_notification)
    session.commit()
    session.refresh(db_notification)
    return db_notification