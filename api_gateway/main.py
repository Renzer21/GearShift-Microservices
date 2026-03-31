from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(
    title="GearShift API Gateway", 
    description="The single entry point routing to all 4 microservices."
)

PARTS_URL = "http://localhost:8001/parts/"
CUSTOMERS_URL = "http://localhost:8002/customers/"
ORDERS_URL = "http://localhost:8003/orders/"
SUPPLIERS_URL = "http://localhost:8004/suppliers/"

class Part(BaseModel):
    name: str
    bike_model: str
    price: float

class Customer(BaseModel):
    name: str
    phone: str
    shop_name: str

class Order(BaseModel):
    customer_name: str
    part_name: str
    quantity: int

class Supplier(BaseModel):
    brand_name: str
    contact_email: str

@app.post("/api/parts/", tags=["Parts API"])
async def create_part(part: Part):
    async with httpx.AsyncClient() as client:
        response = await client.post(PARTS_URL, json=part.dict())
        return response.json()

@app.get("/api/parts/", tags=["Parts API"])
async def get_all_parts():
    async with httpx.AsyncClient() as client:
        response = await client.get(PARTS_URL)
        return response.json()

@app.get("/api/parts/{id}", tags=["Parts API"])
async def get_single_part(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PARTS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Part not found in microservice")
        return response.json()

@app.put("/api/parts/{id}", tags=["Parts API"])
async def update_part(id: str, part: Part):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{PARTS_URL}{id}", json=part.dict())
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Part not found in microservice")
        return response.json()

@app.delete("/api/parts/{id}", tags=["Parts API"])
async def delete_part(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{PARTS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Part not found in microservice")
        return response.json()


@app.post("/api/customers/", tags=["Customers API"])
async def create_customer(customer: Customer):
    async with httpx.AsyncClient() as client:
        response = await client.post(CUSTOMERS_URL, json=customer.dict())
        return response.json()

@app.get("/api/customers/", tags=["Customers API"])
async def get_all_customers():
    async with httpx.AsyncClient() as client:
        response = await client.get(CUSTOMERS_URL)
        return response.json()

@app.get("/api/customers/{id}", tags=["Customers API"])
async def get_single_customer(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{CUSTOMERS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Customer not found")
        return response.json()

@app.put("/api/customers/{id}", tags=["Customers API"])
async def update_customer(id: str, customer: Customer):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{CUSTOMERS_URL}{id}", json=customer.dict())
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Customer not found")
        return response.json()

@app.delete("/api/customers/{id}", tags=["Customers API"])
async def delete_customer(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{CUSTOMERS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Customer not found")
        return response.json()

@app.post("/api/orders/", tags=["Orders API"])
async def create_order(order: Order):
    async with httpx.AsyncClient() as client:
        response = await client.post(ORDERS_URL, json=order.dict())
        return response.json()

@app.get("/api/orders/", tags=["Orders API"])
async def get_all_orders():
    async with httpx.AsyncClient() as client:
        response = await client.get(ORDERS_URL)
        return response.json()

@app.get("/api/orders/{id}", tags=["Orders API"])
async def get_single_order(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ORDERS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Order not found")
        return response.json()

@app.put("/api/orders/{id}", tags=["Orders API"])
async def update_order(id: str, order: Order):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{ORDERS_URL}{id}", json=order.dict())
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Order not found")
        return response.json()

@app.delete("/api/orders/{id}", tags=["Orders API"])
async def delete_order(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{ORDERS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Order not found")
        return response.json()

@app.post("/api/suppliers/", tags=["Suppliers API"])
async def create_supplier(supplier: Supplier):
    async with httpx.AsyncClient() as client:
        response = await client.post(SUPPLIERS_URL, json=supplier.dict())
        return response.json()

@app.get("/api/suppliers/", tags=["Suppliers API"])
async def get_all_suppliers():
    async with httpx.AsyncClient() as client:
        response = await client.get(SUPPLIERS_URL)
        return response.json()

@app.get("/api/suppliers/{id}", tags=["Suppliers API"])
async def get_single_supplier(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SUPPLIERS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return response.json()

@app.put("/api/suppliers/{id}", tags=["Suppliers API"])
async def update_supplier(id: str, supplier: Supplier):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{SUPPLIERS_URL}{id}", json=supplier.dict())
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return response.json()

@app.delete("/api/suppliers/{id}", tags=["Suppliers API"])
async def delete_supplier(id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{SUPPLIERS_URL}{id}")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return response.json()
