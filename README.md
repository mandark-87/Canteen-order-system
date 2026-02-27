🍽️ Campus Canteen Ordering System

A modern full-stack self-ordering web application built for campus canteens.
Students can browse menu items, add to cart, choose payment methods, and receive a unique token for order tracking.

🚀 Live Features
🧾 1️⃣ Interactive Food Menu
![Menu](https://github.com/user-attachments/assets/9e7bf218-0276-42a1-9b38-119b0b24f477)
Categorized sections (Main Course, Beverages, Desserts)
Real-time quantity increase/decrease
Dynamic price calculation

🛒 2️⃣ Smart Cart System
![Cart](https://github.com/user-attachments/assets/d66a8a63-b30a-4d82-bc8d-accc1ed8f8e9)
View selected items
Modify quantity
Auto total calculation
Clean checkout UI

💳 3️⃣ Multiple Payment Methods
✅ UPI Payment
![UPI](https://github.com/user-attachments/assets/1dabac0b-decf-479c-ab97-aa729791aea6)
- Secure UPI input  
- Order summary display  
- Dynamic total
---

✅ Credit/Debit Card
![Card](https://github.com/user-attachments/assets/abbca28c-4709-441d-bf09-7d5e7b3b576e)
- Card number validation  
- Expiry & CVV input  
- Clean modern UI
---

✅ Cash at Counter
![Cash](https://github.com/user-attachments/assets/b88aed04-02c4-471d-be2a-73f586a49301)
- Pay at counter option  
- Total amount display  
- Confirm payment  
Dynamic forms appear based on selected payment method.

🎫 4️⃣ Automatic Token Generation
# 📸 Application Screenshots

## 🏠 Menu Page
![Menu](https://github.com/user-attachments/assets/9e7bf218-0276-42a1-9b38-119b0b24f477)

- Categorized food items  
- Quantity controls (+ / -)  
- Dynamic cart update  

---

## 🛒 Cart Page
![Cart](https://github.com/user-attachments/assets/d66a8a63-b30a-4d82-bc8d-accc1ed8f8e9)

- View selected items  
- Real-time total calculation  
- Proceed to payment  

---

## 💳 UPI Payment
![UPI](https://github.com/user-attachments/assets/1dabac0b-decf-479c-ab97-aa729791aea6)

- Secure UPI input  
- Order summary display  
- Dynamic total  

---

## 💳 Card Payment
![Card](https://github.com/user-attachments/assets/abbca28c-4709-441d-bf09-7d5e7b3b576e)

- Card number validation  
- Expiry & CVV input  
- Clean modern UI  

---

## 💵 Cash at Counter
![Cash](https://github.com/user-attachments/assets/b88aed04-02c4-471d-be2a-73f586a49301)

- Pay at counter option  
- Total amount display  
- Confirm payment  

---

## 🎫 Order Confirmation & Token
![Token](https://github.com/user-attachments/assets/2204180e-9ccf-4b49-99e3-8e17e58cdbe6)

- Unique token number  
- Estimated waiting time  
- Order summary  

---

## 🗄️ MongoDB Order Storage
![MongoDB](https://github.com/user-attachments/assets/b514947d-e8cf-4d17-aa42-c57a6b531aa1)

- Orders stored with:
  - Token number  
  - Payment method  
  - Total amount  
  - Status  
  - Timestamps  
Unique 4-digit token generated per order
Estimated waiting time display
Order confirmation page
Token stored in MongoDB

📦 5️⃣ MongoDB Order Storage
![MongoDB](https://github.com/user-attachments/assets/b514947d-e8cf-4d17-aa42-c57a6b531aa1)

Each order stores:
Items list
Total amount
Payment method
Token number
Status (preparing/completed)
Created & updated timestamps

🛠️ Admin / Database View
View orders in MongoDB Compass
Track:
Order totals
Payment type
Token numbers
Status updates

🛠️ Tech Stack
🔹 Frontend
HTML5
CSS3 (Custom UI + Gradients + Animations)
JavaScript (Dynamic cart & payment logic)
🔹 Backend
Python
Flask
🔹 Database
MongoDB

PyMongo
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/mandark-87/canteen-ordering-system.git

2️⃣ Create Virtual Environment
cd canteen-ordering-system
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Start MongoDB
Make sure MongoDB is running locally:
mongodb://localhost:27017

5️⃣ Run Flask App
python app.py
Open in browser:
http://127.0.0.1:5000
🗄️ Sample Order Document (MongoDB)
{
  "items": [...],
  "total": 510,
  "token": 5900,
  "payment_method": "cash",
  "customer_name": "Anonymous",
  "status": "preparing",
  "estimated_time": 15,
  "created_at": "2025-02-27T10:07:21"
}

🎯 Key Highlights

✔ Clean modern UI
✔ Fully dynamic cart
✔ Real token system
✔ MongoDB integration
✔ Production-ready structure
✔ Beginner-friendly code

📌 Future Improvements
🔐 User login system
📊 Admin dashboard UI
📱 Mobile responsiveness enhancement
📈 Order analytics panel
💬 SMS/WhatsApp token notification

👨‍💻 Author

Mandar Ramchandra Kulkarni
BCA | Full Stack Developer
📍 Karnataka, India
🔗 GitHub: https://github.com/mandark-87
