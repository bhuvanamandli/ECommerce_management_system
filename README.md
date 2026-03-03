🛒 E-Commerce System

A simple E-Commerce Desktop Application built using Python and Tkinter.
This application simulates an online shopping system with user authentication, cart management, order processing, and an admin dashboard.


📌 Project Overview
This project demonstrates:
    - User Login & Account Creation
    - Product Listing & Search
    - Cart Management
    - Order Processing
    - Order History
    - Admin Dashboard
    - Most Purchased Product Analytics
    - User-level Data Isolation with Access Control
        (Each user can access only their own data, and other users cannot see it.)


🏗️ Project Structure
E_Commerce_System/
    │
    ├── main.py          # Entry point of the application
    ├── ecommerce.py     # Main application logic and UI
    ├── database.py      # Data models (Product, Cart, OrderManager)
    ├── README.md        # Project documentation


🚀 Features
    i. 👤 User Features
        - Login with credentials
        - Create new account
        - Search products
        - Add products to cart
        - Remove items from cart
        - View cart total
        - Make payment
        - View order history
        - Logout

    ii. 🔐 Admin Features
        - Admin login
        - View all products
        - View all user orders
        - View most purchased product
        - Logout


🧠 System Design
    i. 📦 Product
        - Represents a product with:
            Name
            Price
        - Products are randomly generated using:
            faker
            faker_commerce

    ii. 🛍️ Cart
        - Stores items per user in the format:
            {
                username: {
                    product_name: quantity
                }
            }

    iii. 📑 Order Manager
        - Stores order records in memory:
        (username, product_name, quantity, total, timestamp)

    iv. 🖥️ How to Run
        - 1️⃣ Install Dependencies
            pip install tkinter
            pip install faker
            pip install faker faker-commerce
        - 2️⃣ Run the Application
            python main.py


📊 Technologies Used
    - Python 3.x
    - Tkinter (GUI)
    - Faker (Random Product Generation)
    - Collections (Counter)
    - OOP Concepts


⚙️ Application Flow
    - Application starts → Login Screen
        User Creates an account/ logs into the existing account

    - User logs in:
        If Admin → Admin Dashboard
        If User → Shopping Panel

    - User:
        - Searches products
        - Adds to cart/Removes from cart
        - Makes payment
        - View Order History

    - Admin:
        - Views all products
        - Views all orders
        - Checks most purchased product


📌 Validation Rules
    - Account Creation
        Username must:
            Be alphanumeric
            Be less than 7 characters

        Name must:
            Be less than 8 characters
            Contain no spaces

        Password must:
            Be less than 12 characters


📦 Data Storage
    ⚠️ Note:
        - This application uses in-memory storage only.
        - All data (cart & orders) will be lost after closing the application.
        - No external database is used.