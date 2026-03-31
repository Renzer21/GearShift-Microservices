from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI(title="Parts Service")

# Connect to MongoDB
client = AsyncIOMotorClient("mongodb+srv://vihanga1:Srilanka1234@cluster0.vkq9t3u.mongodb.net/gearshop")
db = client.gearshift_parts

class Part(BaseModel):
    name: str
    bike_model: str
    price: float

@app.post("/parts/")
async def add_part(part: Part):
    new_part = await db.parts.insert_one(part.dict())
    return {"message": "Part added successfully", "id": str(new_part.inserted_id)}

@app.get("/parts/")
async def get_all_parts():
    parts = await db.parts.find().to_list(100)
    for part in parts:
        part["_id"] = str(part["_id"])
    return parts

# NEW: Get a single part by its ID
@app.get("/parts/{id}")
async def get_part(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    part = await db.parts.find_one({"_id": ObjectId(id)})
    if part:
        part["_id"] = str(part["_id"])
        return part
    raise HTTPException(status_code=404, detail="Part not found")

# NEW: Update an existing part
@app.put("/parts/{id}")
async def update_part(id: str, part: Part):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    result = await db.parts.update_one({"_id": ObjectId(id)}, {"$set": part.dict()})
    if result.modified_count == 1:
        return {"message": "Part updated successfully"}
    raise HTTPException(status_code=404, detail="Part not found")

# NEW: Delete a part
@app.delete("/parts/{id}")
async def delete_part(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")
    result = await db.parts.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Part deleted successfully"}
    raise HTTPException(status_code=404, detail="Part not found")