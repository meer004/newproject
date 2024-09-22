from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/payments/")
def Create_payment(
    id: int ,
    amount: float,
    email: str,
    payment_status: str 
):
 print(f"payment: id= {id},amount= {amount},email = {email}, status={payment_status}")
 return("message", "Payment created successfully")


@app.get("/payment")
async def get_payment(id: int,amount: float,email: str,payment_status: str):
    # Replace with  payment 
    print(f"Fetching payment with ID: {id}")
    return {"message": "Payment retrieved successfully"}
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment 
data = []
@app.delete("/payments/{id}")
def update_payment(id: int,email: str, amount: float):
  data.append(id)
  data.append(email)
  data.append(amount)
  return data  

  