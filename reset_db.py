from app import create_app
from app import mongo
from datetime import datetime

app = create_app()

with app.app_context():
    print("🟢 Resetting MongoDB database...")
    
    # Drop existing collections
    mongo.db.menu_items.drop()
    mongo.db.orders.drop()
    print("🗑️ Collections dropped")
    
    # Insert sample menu items
    sample_items = [
        {
            "name": "Chicken Biryani",
            "price": 180,
            "category": "main",
            "description": "Fragrant basmati rice with tender chicken and aromatic spices",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Paneer Butter Masala", 
            "price": 160,
            "category": "main",
            "description": "Soft cottage cheese in rich, creamy tomato gravy",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Veg Fried Rice",
            "price": 120,
            "category": "main", 
            "description": "Stir-fried rice with fresh vegetables and soy sauce",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Cold Coffee",
            "price": 80,
            "category": "beverage",
            "description": "Chilled coffee with milk and ice cream", 
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Fresh Lime Soda",
            "price": 50,
            "category": "beverage",
            "description": "Refreshing lime juice with soda and mint",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Masala Chai",
            "price": 30,
            "category": "beverage", 
            "description": "Traditional Indian tea with aromatic spices",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Chocolate Brownie",
            "price": 90,
            "category": "dessert",
            "description": "Warm chocolate brownie with vanilla ice cream",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Gulab Jamun", 
            "price": 60,
            "category": "dessert",
            "description": "Soft milk dumplings in sweet syrup",
            "image_url": "",
            "available": True,
            "created_at": datetime.utcnow()
        },
        {
            "name": "Ice Cream Scoop",
            "price": 50,
            "category": "dessert",
            "description": "Single scoop of premium ice cream",
            "image_url": "",
            "available": True, 
            "created_at": datetime.utcnow()
        }
    ]
    
    result = mongo.db.menu_items.insert_many(sample_items)
    print(f"✅ Added {len(result.inserted_ids)} menu items to MongoDB!")
    
    # Verify the data was inserted
    count = mongo.db.menu_items.count_documents({})
    print(f"✅ Total menu items in database: {count}")