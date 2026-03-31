from fastapi import FastAPI, HTTPException
from bson import ObjectId
from models import Customer         
from database import customer_collection 

app = FastAPI(title="Customer Service")

@app.post("/customers/")
async def add_customer(customer: Customer):
    new_cust = await customer_collection.insert_one(customer.dict())
    return {"message": "Customer added", "id": str(new_cust.inserted_id)}

@app.get("/customers/")
async def get_customers():
    customers = await customer_collection.find().to_list(100)
    for c in customers:
        c["_id"] = str(c["_id"])
    return customers

