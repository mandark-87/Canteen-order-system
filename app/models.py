from app import mongo
from bson.objectid import ObjectId
from datetime import datetime

def init_mongodb():
    """Initialize MongoDB with sample data"""
    try:
        # Check connection
        mongo.db.command('ping')
        print("✅ MongoDB connected successfully!")
        
        # Create collections if they don't exist and insert sample data
        if mongo.db.menu_items.count_documents({}) == 0:
            sample_items = [
                {
                    "name": "Ice Cream Scoop",
                    "price": 4.99,
                    "category": "dessert",
                    "description": "Single scoop of premium ice cream",
                    "image_url": "",
                    "available": True,
                    "created_at": datetime.utcnow()
                },
                {
                    "name": "Chocolate Brownie", 
                    "price": 6.99,
                    "category": "dessert",
                    "description": "Warm chocolate brownie with vanilla ice cream",
                    "image_url": "",
                    "available": True,
                    "created_at": datetime.utcnow()
                },
                {
                    "name": "Mango Shake",
                    "price": 5.99,
                    "category": "beverage",
                    "description": "Creamy mango milkshake with ice cream", 
                    "image_url": "",
                    "available": True,
                    "created_at": datetime.utcnow()
                },
                {
                    "name": "Masala Chai",
                    "price": 3.99,
                    "category": "beverage",
                    "description": "Traditional Indian tea with aromatic spices",
                    "image_url": "",
                    "available": True,
                    "created_at": datetime.utcnow()
                },
                {
                    "name": "Lime Soda",
                    "price": 4.49,
                    "category": "beverage",
                    "description": "Refreshing lime juice with soda and mint",
                    "image_url": "",
                    "available": True,
                    "created_at": datetime.utcnow()
                }
            ]
            
            mongo.db.menu_items.insert_many(sample_items)
            print("✅ MongoDB initialized with sample menu items!")
        else:
            print("✅ MongoDB already contains data")
            
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")

def get_menu_items():
    """Get all available menu items"""
    return list(mongo.db.menu_items.find({"available": True}))

def get_menu_item_by_id(item_id):
    """Get menu item by ID"""
    try:
        return mongo.db.menu_items.find_one({"_id": ObjectId(item_id), "available": True})
    except:
        return None

def create_order(order_data):
    """Create a new order"""
    order_data["created_at"] = datetime.utcnow()
    order_data["status"] = order_data.get("status", "preparing")
    
    result = mongo.db.orders.insert_one(order_data)
    return result.inserted_id

def get_all_orders():
    """Get all orders"""
    return list(mongo.db.orders.find().sort("created_at", -1))

def update_order_status(order_id, status):
    """Update order status"""
    try:
        result = mongo.db.orders.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"status": status, "updated_at": datetime.utcnow()}}
        )
        return result
    except:
        return None

def get_order_by_id(order_id):
    """Get order by MongoDB ObjectId"""
    try:
        return mongo.db.orders.find_one({"_id": ObjectId(order_id)})
    except:
        return None