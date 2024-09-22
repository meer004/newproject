from fastapi import FastAPI, Request

app = FastAPI()
orders=[]
@app.post("/orders/")
def create_order(customer_name, id, items, price, status): 
  order = {
      'customer_name': customer_name,
      'id': len(orders)+1, 
      'items':items,
      'price':price,
      'status': 'pending' 
  }
  orders.append(order) 

@app.get("/orders/{id}")
def read_order(id):
  for order in orders:
    if order['id'] == id:
      return order
  return None 

@app.put("/orders/{id}")
def update_order(id: int, update: dict):
  order = read_order(id)
  if order: 
    order.update(update)
    return order
  return None

@app.delete("/orders/{id}")
def delete_order(id: int):
  order = read_order(id)
  if order:
    orders.remove(order)
    return True