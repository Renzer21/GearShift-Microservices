from motor.motor_asyncio import AsyncIOMotorClient

# ඔයාගේ MongoDB URL එක මෙතන තියෙනවා
MONGO_DETAILS = "mongodb+srv://vihanga1:Srilanka1234@cluster0.vkq9t3u.mongodb.net/gearshop"

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.gearshift_customers
customer_collection = db.customers