from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from inventryservice import crud, models, schemas
from inventryservice.db import create_db_and_tables, get_session

app = FastAPI()

# Create the database and tables
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Create a new inventory item
@app.post("/inventory/", response_model=schemas.InventoryItemRead)
def create_inventory_item(
    item: schemas.InventoryItemCreate, session: Session = Depends(get_session)
):
    return crud.create_inventory_item(session=session, item=item)

# Get a specific inventory item by ID
@app.get("/inventory/{item_id}", response_model=schemas.InventoryItemRead)
def get_inventory_item(item_id: int, session: Session = Depends(get_session)):
    db_item = crud.get_inventory_item(session=session, item_id=item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Get a list of inventory items
@app.get("/inventory/", response_model=list[schemas.InventoryItemRead])
def get_inventory_items(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return crud.get_inventory_items(session=session, skip=skip, limit=limit)

# Update an existing inventory item
@app.put("/inventory/{item_id}", response_model=schemas.InventoryItemRead)
def update_inventory_item(
    item_id: int, item: schemas.InventoryItemUpdate, session: Session = Depends(get_session)
):
    db_item = crud.update_inventory_item(session=session, item_id=item_id, item=item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Delete an inventory item
@app.delete("/inventory/{item_id}")
def delete_inventory_item(item_id: int, session: Session = Depends(get_session)):
    result = crud.delete_inventory_item(session=session, item_id=item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result
