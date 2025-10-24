from flask import Blueprint, jsonify, request
from bson import ObjectId
from bson.errors import InvalidId
import random
from datetime import datetime
import json 
try:
    from app.models import get_menu_items, create_order, get_menu_item_by_id, get_all_orders, update_order_status
    # MongoDB is available
    mongo_available = True
    mongo_db = None  # We don't need direct db access since we use the functions
except ImportError:
    # Fallback - MongoDB functions not available
    mongo_available = False
    mongo_db = None
    
    # Define fallback functions or import SQLite versions
    def get_menu_items():
        return []
    
    def create_order(order_data):
        return "temp_id"
    
    # Add other fallback functions as needed

bp = Blueprint('main', __name__)

# MongoDB collections
if mongo_available and mongo_db is not None:
    menu_items = mongo_db.menu_items
    orders = mongo_db.orders
else:
    menu_items = None
    orders = None

# Initialize database
#init_sqlite_db()

# Add these routes to see MongoDB data

@bp.route('/api/mongo/menu')
def get_mongo_menu():
    """Get menu items from MongoDB"""
    try:
        if not mongo_available or menu_items is None:
            return jsonify({'success': False, 'error': 'MongoDB not available'}), 500
        
        items = list(menu_items.find({}, {'_id': 0}))
        return jsonify({
            'success': True,
            'count': len(items),
            'source': 'mongodb',
            'items': items
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/mongo/orders')
def get_mongo_orders():
    """Get orders from MongoDB"""
    try:
        if not mongo_available or orders is None:
            return jsonify({'success': False, 'error': 'MongoDB not available'}), 500
        
        mongo_orders_list = list(orders.find({}))
        
        # Convert ObjectId to string for JSON serialization
        for order in mongo_orders_list:
            order['_id'] = str(order['_id'])
        
        return jsonify({
            'success': True,
            'count': len(mongo_orders_list),
            'source': 'mongodb',
            'orders': mongo_orders_list
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/mongo/stats')
def get_mongo_stats():
    """Get MongoDB statistics"""
    try:
        if not mongo_available or mongo_db is None:
            return jsonify({'success': False, 'error': 'MongoDB not available'}), 500
        
        menu_count = menu_items.count_documents({}) if menu_items is not None else 0
        orders_count = orders.count_documents({}) if orders is not None else 0
        
        return jsonify({
            'success': True,
            'database': 'mongodb',
            'stats': {
                'menu_items_count': menu_count,
                'orders_count': orders_count,
                'collections': mongo_db.list_collection_names() if mongo_db is not None else []
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/sync-to-mongo')
def sync_to_mongo():
    """MongoDB status check - sync not needed since we're using MongoDB"""
    try:
        if not mongo_available:
            return jsonify({'success': False, 'error': 'MongoDB not available'}), 500
        
        # Just return MongoDB status since we're already using it
        menu_count = len(get_menu_items())
        orders_count = len(get_all_orders())
        
        return jsonify({
            'success': True,
            'message': 'MongoDB is already the primary database - no sync needed',
            'stats': {
                'menu_items': menu_count,
                'orders': orders_count
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
        
        # Sync orders
        c.execute("SELECT * FROM orders")
        sqlite_orders = c.fetchall()
        
        for order in sqlite_orders:
            order_dict = dict(order)
            order_dict.pop('_id', None)
            order_dict['items'] = json.loads(order_dict['items'])
            # Insert or update in MongoDB
            if orders is not None:
                orders.update_one(
                    {'order_id': order_dict['id']},
                    {'$set': order_dict},
                    upsert=True
                )
        
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Data synced to MongoDB',
            'menu_items_synced': len(sqlite_menu),
            'orders_synced': len(sqlite_orders)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    
# Helper functions
def generate_unique_token():
    """Generate a unique 4-digit token"""
    if not mongo_available or orders is None:
        return random.randint(1000, 9999)
    
    max_attempts = 100
    attempts = 0
    
    while attempts < max_attempts:
        token = random.randint(1000, 9999)
        existing = orders.find_one({'token': token}) if orders is not None else None
        if not existing:
            return token
        attempts += 1
    
    # Fallback: use timestamp-based token
    return int(datetime.now().strftime("%H%M%S"))

def calculate_estimated_time(items):
    """Calculate estimated preparation time based on items"""
    base_time = 5  # Base preparation time
    max_item_time = 0
    
    if not mongo_available or menu_items is None:
        return base_time + 10  # Default estimate
    
    for item in items:
        if menu_items is not None:
            menu_item = menu_items.find_one({'id': item['id']})
            if menu_item and 'prep_time' in menu_item:
                item_prep_time = menu_item['prep_time'] * item['quantity']
                max_item_time = max(max_item_time, item_prep_time)
    
    return base_time + max_item_time

# API Routes - USE @bp.route INSTEAD OF @app.route
@bp.route('/')
def home():
    return jsonify({
        "message": "🍽️ Canteen API is running!", 
        "database": "MongoDB + SQLite",
        "version": "2.0",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "health": "/api/health",
            "menu": "/api/menu",
            "categories": "/api/menu/categories",
            "create_order": "/api/order (POST)",
            "get_orders": "/api/orders",
            "stats": "/api/stats"
        }
    })

@bp.route('/api/health')
def health_check():
    try:
        # Test MongoDB connection only
        mongo_status = "connected" if mongo_available else "disconnected"
        
        if mongo_available:
            menu_count = len(get_menu_items())
            orders_count = len(get_all_orders())
        else:
            menu_count = 0
            orders_count = 0
        
        return jsonify({
            'status': 'healthy',
            'database': {
                'mongodb': mongo_status
            },
            'timestamp': datetime.now().isoformat(),
            'collections': {
                'menu_items': menu_count,
                'orders': orders_count
            },
            'system': {
                'server_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'uptime': 'running'
            }
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@bp.route('/api/menu')
def get_menu():
    try:
        print("🟢 /api/menu endpoint hit")
        # Get from MongoDB
        menu_items_mongo = get_menu_items()
        print(f"🟢 Found {len(menu_items_mongo)} menu items from MongoDB")
        
        # Convert to list of dictionaries and convert ObjectId to string
        menu = []
        for item in menu_items_mongo:
            item_dict = dict(item)
            item_dict['_id'] = str(item_dict['_id'])  # Convert ObjectId to string
            menu.append(item_dict)
        
        print(f"🟢 Returning {len(menu)} items")
        return jsonify({
            'success': True,
            'count': len(menu),
            'source': 'mongodb',
            'items': menu
        })
    except Exception as e:
        print(f"🔴 ERROR in /api/menu: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500
    
@bp.route('/api/menu/<item_id>')
def get_menu_item(item_id):
    try:
        # Get from MongoDB using the function from models.py
        item = get_menu_item_by_id(item_id)
        
        if item:
            # Convert ObjectId to string for JSON serialization
            item['_id'] = str(item['_id'])
            return jsonify({'success': True, 'item': item})
        return jsonify({'success': False, 'error': 'Item not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/menu/categories')
def get_categories():
    try:
        # Get all menu items from MongoDB
        menu_items = get_menu_items()
        
        # Extract unique categories and count items per category
        categories = list(set(item['category'] for item in menu_items))
        
        category_counts = {}
        for category in categories:
            count = len([item for item in menu_items if item['category'] == category])
            category_counts[category] = count
        
        return jsonify({
            'success': True,
            'categories': categories,
            'counts': category_counts,
            'total_categories': len(categories)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/order', methods=['POST'])
def create_order_route():  # ← Change function name
    try:
        print("🟢 /api/order endpoint hit")
        order_data = request.get_json()
        print(f"🟢 Order data received: {order_data}")
        
        # Validate required fields
        if not order_data:
            print("🔴 No order data")
            return jsonify({'success': False, 'error': 'No data provided'}), 400
            
        if 'items' not in order_data or not order_data['items']:
            print("🔴 No items in order")
            return jsonify({'success': False, 'error': 'Items are required'}), 400
        
        print(f"🟢 Processing {len(order_data['items'])} items")
        
        # Validate items structure and calculate total
        total = 0
        valid_items = []
        
        for item in order_data['items']:
            print(f"🟢 Processing item: {item}")
            if 'id' not in item or 'quantity' not in item:
                return jsonify({'success': False, 'error': 'Each item must have id and quantity'}), 400
            
            # Get item price from MongoDB
            menu_item = get_menu_item_by_id(item['id'])
            
            if menu_item:
                print(f"🟢 Found menu item: {menu_item['name']} - ${menu_item['price']}")
                item_total = menu_item['price'] * item['quantity']
                total += item_total
                valid_items.append({
                    'id': str(menu_item['_id']),  # Convert ObjectId to string
                    'name': menu_item['name'],
                    'price': float(menu_item['price']),
                    'quantity': item['quantity'],
                    'item_total': float(item_total)
                })
            else:
                print(f"🔴 Menu item not found: ID {item['id']}")
        
        print(f"🟢 Total calculated: {total}")
        print(f"🟢 Valid items: {len(valid_items)}")
        
        if not valid_items:
            print("🔴 No valid items found")
            return jsonify({'success': False, 'error': 'No valid items found'}), 400
        
        # Generate unique token
        token = generate_unique_token()
        print(f"🟢 Generated token: {token}")
        
        # Create order data for MongoDB
        order_doc = {
            'items': valid_items,
            'total': float(total),
            'token': token,
            'payment_method': order_data.get('payment_method', 'cash'),
            'customer_name': order_data.get('customer_name', 'Walk-in Customer'),
            'customer_phone': order_data.get('customer_phone', ''),
            'special_instructions': order_data.get('special_instructions', ''),
            'status': 'preparing',
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'estimated_time': calculate_estimated_time(order_data['items'])
        }
        
        # Insert into MongoDB - FIXED: call the model function
        order_id = create_order(order_doc)  # This now calls the model function
        print(f"🟢 Order inserted into MongoDB with ID: {order_id}")
        
        print(f"🟢 Order completed successfully! ID: {order_id}, Token: {token}")
        return jsonify({
            'success': True,
            'order_id': str(order_id),
            'token': token,
            'total': total,
            'status': 'preparing',
            'estimated_time': calculate_estimated_time(order_data['items']),
            'message': 'Order placed successfully! Please remember your token for order tracking.'
        })
        
    except Exception as e:
        print(f"🔴 ERROR in /api/order: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500
    
@bp.route('/api/order/<order_id>')
def get_order(order_id):
    try:
        # Get order from MongoDB using the function from models.py
        from app.models import get_order_by_id
        order = get_order_by_id(order_id)
        
        if order:
            # Convert ObjectId and datetime for JSON serialization
            order['_id'] = str(order['_id'])
            if 'created_at' in order:
                order['created_at'] = order['created_at'].isoformat()
            if 'updated_at' in order:
                order['updated_at'] = order['updated_at'].isoformat()
            return jsonify({'success': True, 'order': order})
        return jsonify({'success': False, 'error': 'Order not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/order/token/<token>')
def get_order_by_token(token):
    try:
        # Get all orders and filter by token
        orders = get_all_orders()
        order = next((o for o in orders if o.get('token') == int(token)), None)
        
        if order:
            # Convert ObjectId and datetime for JSON serialization
            order['_id'] = str(order['_id'])
            if 'created_at' in order:
                order['created_at'] = order['created_at'].isoformat()
            if 'updated_at' in order:
                order['updated_at'] = order['updated_at'].isoformat()
            return jsonify({'success': True, 'order': order})
        return jsonify({'success': False, 'error': 'Order not found with this token'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/orders')
def get_all_orders_route():  # ← Change function name
    try:
        orders = get_all_orders()  # ← Now calls the model function
        
        # Convert ObjectId and datetime for JSON serialization
        orders_list = []
        for order in orders:
            order_dict = dict(order)
            order_dict['_id'] = str(order_dict['_id'])
            if 'created_at' in order_dict:
                order_dict['created_at'] = order_dict['created_at'].isoformat()
            if 'updated_at' in order_dict:
                order_dict['updated_at'] = order_dict['updated_at'].isoformat()
            orders_list.append(order_dict)
        
        return jsonify({
            'success': True,
            'count': len(orders_list),
            'orders': orders_list
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/order/<order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    try:
        status_data = request.get_json()
        new_status = status_data.get('status')
        
        if not new_status:
            return jsonify({'success': False, 'error': 'Status is required'}), 400
        
        valid_statuses = ['preparing', 'ready', 'completed', 'cancelled']
        if new_status not in valid_statuses:
            return jsonify({'success': False, 'error': f'Invalid status. Must be one of: {", ".join(valid_statuses)}'}), 400
        
        # Update order status in MongoDB
        result = update_order_status(order_id, new_status)
        
        if result and result.modified_count:
            return jsonify({
                'success': True, 
                'message': 'Order status updated successfully',
                'new_status': new_status,
                'order_id': order_id
            })
        return jsonify({'success': False, 'error': 'Order not found'}), 404
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@bp.route('/api/stats')
def get_stats():
    try:
        # MongoDB stats
        orders = get_all_orders()
        menu_items = get_menu_items()
        
        # Calculate stats
        total_orders = len(orders)
        total_revenue = sum(order.get('total', 0) for order in orders)
        
        # Status counts
        status_counts = {}
        for order in orders:
            status = order.get('status', 'unknown')
            status_counts[status] = status_counts.get(status, 0) + 1
        
        # Today's orders
        from datetime import datetime, date
        today = date.today()
        today_orders = len([o for o in orders if o.get('created_at') and o['created_at'].date() == today])
        
        # Menu items count
        menu_items_count = len(menu_items)
        available_items = len([item for item in menu_items if item.get('available', True)])
        
        return jsonify({
            'success': True,
            'stats': {
                'total_orders': total_orders,
                'total_revenue': round(total_revenue, 2),
                'today_orders': today_orders,
                'status_breakdown': [{'status': k, 'count': v} for k, v in status_counts.items()],
                'menu_items_count': menu_items_count,
                'available_items': available_items
            },
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Error handlers (keep these as they are)
@bp.app_errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False, 
        'error': 'Endpoint not found',
        'message': 'The requested API endpoint does not exist.'
    }), 404

@bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False, 
        'error': 'Internal server error',
        'message': 'Something went wrong on our server. Please try again later.'
    }), 500

@bp.app_errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'success': False,
        'error': 'Method not allowed',
        'message': 'The HTTP method is not supported for this endpoint.'
    }), 405