from fastapi import FastAPI,Depends,HTTPException 
from sqlmodel import Session 
from productservice.db import create_db_and_tables,get_session
from productservice.schems import ProductCreate,ProductRead
from productservice.crud import create_product, get_product_by_id,get_products
from typing import List
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield
app=FastAPI(lifespan=lifespan)

@app.get("/")
def product():
    return {"This is my mart project"}

@app.get("/products")
def get_products(db: Session= Depends(get_session)):
    get_all_products = get_products(session=db)
    if not get_all_products:
        raise HTTPException(status_code=404,detail="Products not found")
    return get_all_products


@app.post("/products/", response_model=ProductRead)
def create_new_product(product:ProductCreate,db:Session=Depends(get_session)):
    db_product=create_product(session=db,product=product)
    return db_product
@app.get("/products/{product_id}")
def read_product(product_id:int, db:Session=Depends(get_session)):
    db_product=get_product_by_id(session=db,product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404,detail="Product not found")
    return db_product
    