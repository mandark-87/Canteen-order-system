<<<<<<< HEAD
🍽️ Campus Canteen Ordering System

A modern full-stack self-ordering web application built for campus canteens.
Students can browse menu items, add to cart, choose payment methods, and receive a unique token for order tracking.

🚀 Live Features

=======
# 🍔 Campus Canteen Ordering System

A modern **Flask-based Campus Canteen Ordering System** that enables students to order food online and allows administrators to efficiently manage menu items and customer orders. The application provides a simple, user-friendly interface with secure authentication and real-time order management.

---

## 📌 Features

### 👨‍🎓 Student Module
- User Registration & Login
- Browse Food Menu
- Add Items to Cart
- Place Orders
- View Order History
- Order Token Generation
- Responsive User Interface

### 👨‍🍳 Admin Module
- Secure Admin Login
- Add Food Items
- Edit Food Items
- Delete Food Items
- Manage Customer Orders
- Update Order Status
- View All Orders

>>>>>>> 28c2766 (Add remaining project files)
---

## 🏠 Menu Page
![Menu](https://github.com/user-attachments/assets/9e7bf218-0276-42a1-9b38-119b0b24f477)

<<<<<<< HEAD
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
=======
### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Backend
- Python
- Flask

### Database
- MongoDB

### Deployment
- AWS EC2
- Gunicorn
- Nginx

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
Canteen-order-system/
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── templates/
│   ├── static/
│   └── __init__.py
│
├── config.py
├── run.py
├── wsgi.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mandark-87/Canteen-order-system.git
cd Canteen-order-system
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure MongoDB

Update your MongoDB connection string in your configuration file.

Example:

```python
MONGO_URI = "mongodb://localhost:27017/canteen"
```

or

```python
MONGO_URI = "mongodb+srv://<username>:<password>@cluster.mongodb.net/canteen"
```

---

### 5. Run the Application

```bash
python run.py
```

or

```bash
flask run
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## ☁️ AWS Deployment

The application can be deployed on:

- Amazon EC2
- Gunicorn
- Nginx

Deployment Steps:

1. Launch EC2 Instance
2. Connect via SSH
3. Clone Repository
4. Create Virtual Environment
5. Install Requirements
6. Configure Gunicorn
7. Configure Nginx
8. Start Application

---

## 📷 Screenshots

### Home Page

(Add Screenshot)

### Login

(Add Screenshot)

### Menu

(Add Screenshot)

### Cart

(Add Screenshot)

### Admin Dashboard

(Add Screenshot)

---

## 📦 Requirements

```
Flask
Flask-PyMongo
pymongo
gunicorn
python-dotenv
```

Install using

```bash
pip install -r requirements.txt
```

---

## 🔐 Future Enhancements

- Online Payment Integration
- Email Notifications
- QR Code Based Ordering
- Live Order Tracking
- Mobile Responsive UI Improvements
- Analytics Dashboard
- AWS RDS Integration
- Docker Support
- CI/CD using GitHub Actions

---

## 👨‍💻 Author

**Mandar Kulkarni**

GitHub: https://github.com/mandark-87

LinkedIn: https://www.linkedin.com/in/mandarkulkarni/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
>>>>>>> 28c2766 (Add remaining project files)
