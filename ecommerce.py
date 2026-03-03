import tkinter as tk
from tkinter import messagebox
from database import Product, Cart, OrderManager
from collections import Counter
import random as r
from faker import Faker
from faker_commerce import Provider

fake = Faker()
fake.add_provider(Provider)


class EcommerceApp:
    """
    Main Ecommerce Application class.

    Handles:
    - User Authentication
    - Product Listing & Search
    - Cart Management
    - Order Processing
    - Admin Dashboard
    """

    def __init__(self, root):
        """
        Initialize application UI, products, cart and order manager.

        :param root: Tkinter root window
        """
        try:
            self.root = root
            self.root.title("E-Commerce System")
            self.root.geometry("850x650")

            self.products = []            
            unique_names = set()
            while len(unique_names) <= 50:
                name = fake.ecommerce_name()
                unique_names.add(name)

            for name in unique_names:
                self.products.append(
                    Product(name, r.randint(200, 2000))
                )

            self.cart = Cart()
            self.order_manager = OrderManager()
            self.username = ""
            
            self.admin_username = "admin@commerce.com"
            
            self.users = {
                self.admin_username :{
                    "name":"Admin",
                    "password":"admin@123"
                },
                "usera@commerce.com":{
                    "name":"UserA",
                    "password":"usera@123"
                },
                "userb@commerce.com":{
                    "name":"UserB",
                    "password":"userb@123"
                }
            }

            self.login_frame = tk.Frame(root)
            self.account_frame = tk.Frame(root)
            self.user_frame = tk.Frame(root)
            self.cart_frame = tk.Frame(root)
            self.admin_frame = tk.Frame(root)

            self.create_login_frame()
            self.create_account_frame()
            self.create_user_frame()
            self.create_cart_frame()
            self.create_admin_frame()

            self.show_frame(self.login_frame)

        except Exception as e:
            print("Initialization failed")

    # ================= COMMON =================

    def show_frame(self, frame):
        """
        Display selected frame and hide others.
        """
        try:
            for f in (self.login_frame, self.account_frame,
                      self.user_frame,
                      self.cart_frame, self.admin_frame):
                f.pack_forget()
            frame.pack(fill="both", expand=True)
        except Exception:
            print("Error while switching frames")

    # ================= LOGIN =================

    def validate_login_event(self, event):
        """
        Trigger login validation when Enter key is pressed.
        """
        try:
            self.validate_login()
        except Exception:
            print("Login event failed")

    def create_login_frame(self):
        """
        Create login UI components.
        """
        try:
            tk.Label(self.login_frame, text="Login Panel",
                     font=("Arial", 30)).pack(pady=40)

            tk.Label(self.login_frame, text="Username").pack()
            self.username_entry = tk.Entry(self.login_frame, width=30)
            self.username_entry.pack(pady=5)

            tk.Label(self.login_frame, text="Password").pack()
            self.password_entry = tk.Entry(self.login_frame, show="*", width=30)
            self.password_entry.pack(pady=5)
            self.password_entry.bind("<Return>", self.validate_login_event)

            tk.Button(self.login_frame, text="Login",
                      command=self.validate_login).pack(pady=15)
            
            tk.Button(self.login_frame, text="Create Account",
                      command=lambda: self.show_frame(self.account_frame)).pack()
        except Exception:
            print("Error creating login frame")

    def validate_login(self):
        """
        Validate user credentials and redirect to respective panel.
        """
        try:
            username = self.username_entry.get()
            password = self.password_entry.get()
            if not username or not password:
                messagebox.showerror("Login Failed", "Username or Password should not be empty")
            
            else:
                if username in self.users.keys():
                    user_details = self.users[username]
                    if username == self.admin_username and user_details["password"] == password:
                        self.username = user_details["name"]
                        self.password_entry.delete(0, tk.END)
                        self.username_entry.delete(0, tk.END)
                        self.load_admin_data()
                        self.login_label.config(text="Admin Panel")
                        self.show_frame(self.admin_frame)
                        
                    elif user_details["password"] == password:
                        self.username = user_details["name"]
                        self.password_entry.delete(0, tk.END)
                        self.username_entry.delete(0, tk.END)
                        self.login_label.config(text=f"{self.username}'s Shopping Panel")
                        self.show_frame(self.user_frame)

                    else:
                        messagebox.showerror("Login Failed", "Invalid Password")
                        self.password_entry.delete(0, tk.END)
                        
                else:
                    messagebox.showerror("Auth Failed", "Create an account to login")
                    self.password_entry.delete(0, tk.END)
                    self.username_entry.delete(0, tk.END)
        except Exception:
            print("Login validation failed")
            
            
    # ================= ACCOUNT CREATION =================
    def validate_account_details_event(self, event):
        """
        Trigger create account validation when Enter key is pressed.
        """
        try:
            self.validate_account_details()
        except Exception:
            print("Create account event failed")
            
    def create_account_frame(self):
        """
        Create new user account and redirect to login panel.
        """
        try:
            tk.Label(self.account_frame, text="Account Creation Panel",
                     font=('Arial', 30)).pack(pady=40)
            
            tk.Label(self.account_frame, text="Username *").pack()
            username_frame = tk.Frame(self.account_frame)
            username_frame.pack(pady=5)
            self.acc_username_entry = tk.Entry(username_frame, width=13)
            self.acc_username_entry.pack(side="left")
            tk.Label(username_frame, text="@commerce.com").pack(side="left")
            
            tk.Label(self.account_frame, text="Name *").pack()
            self.acc_name_entry = tk.Entry(self.account_frame, width=30)
            self.acc_name_entry.pack(pady=5)
            
            tk.Label(self.account_frame, text="Password *").pack()
            self.acc_password_entry = tk.Entry(self.account_frame, width=30, show='*')
            self.acc_password_entry.pack(pady=5)
            self.acc_password_entry.bind("<Return>", 
                                         self.validate_account_details_event)
            
            tk.Button(self.account_frame, text="Create Account",
                      command=self.validate_account_details).pack(pady=15)
            
            tk.Button(self.account_frame, text="Back",
                      command=lambda: self.show_frame(self.login_frame)).pack()
        except Exception:
            print("Error creating user account frame")
            
    
    def validate_account_details(self):
        """
        Validating User Account details.
        """
        try:
            acc_name = self.acc_name_entry.get()
            acc_username = self.acc_username_entry.get()
            acc_password = self.acc_password_entry.get()
            
            if not acc_name or not acc_username or not acc_password:
                messagebox.showerror("Account Creation", "Please fill all the required fields")

            elif len(acc_username) >= 10:
                messagebox.showerror("Account Creation", "Username must be less than 7 characters")
                
            elif not acc_username.isalnum():
                messagebox.showerror("Account Creation", "Username should only contain alphabets and numbers")
            
            elif len(acc_name) >= 8:
                messagebox.showerror("Account Creation", "Account name must be less than 8 characters")

            elif " " in acc_name:
                messagebox.showerror("Account Creation", "Account name must not contain spaces")

            elif len(acc_password) >= 12:
                messagebox.showerror("Account Creation", "Password must be less than 12 characters")
                

            else:
                acc_username+="@commerce.com"
                self.users[acc_username] = {
                    "name": acc_name,
                    "password": acc_password
                }
                messagebox.showinfo("Account Creation", "Account created successfully")
                self.acc_name_entry.delete(0, tk.END)
                self.acc_username_entry.delete(0, tk.END)
                self.acc_password_entry.delete(0, tk.END)
                self.show_frame(self.login_frame)
        except Exception:
            logging.exception("Account creation failed")
            
    # ================= USER =================

    def create_user_frame(self):
        """
        Create user dashboard UI.
        """
        try:  
            self.login_label = tk.Label(self.user_frame, text="User Panel",
                     font=("Arial", 25))
            self.login_label.pack()

            self.search_entry = tk.Entry(self.user_frame)
            self.search_entry.pack()

            tk.Button(self.user_frame, text="Search",
                      command=self.search_product).pack()

            self.product_list = tk.Listbox(self.user_frame)
            self.product_list.pack(fill="both", expand=True)

            tk.Label(self.user_frame, text="Quantity").pack()
            self.qty_spin = tk.Spinbox(self.user_frame, from_=1, to=5)
            self.qty_spin.pack()

            tk.Button(self.user_frame, text="Add to Cart",
                      command=self.add_to_cart).pack(pady=5)

            tk.Button(self.user_frame, text="View Cart",
                      command=self.open_cart).pack(pady=5)
            
            tk.Button(self.user_frame, text="Order History",
                      command=self.open_history).pack(pady=5)

            tk.Button(self.user_frame, text="Logout",
                      command=self.logout_user).pack(pady=5)

            self.load_products()
        except Exception:
            print("Error creating user frame")

    def logout_user(self):
        """
        Logout current user and reset session data.
        """
        try:
            self.search_entry.delete(0, tk.END)
            self.load_products()
            self.username = ""
            self.qty_spin.delete(0, tk.END)
            self.qty_spin.insert(0, "1")
            self.cart_label.config(text="Your Cart")
            self.login_label.config(text="User Panel")
            self.show_frame(self.login_frame)
        except Exception:
            print("Logout failed")

    def load_products(self):
        """
        Load all available products into listbox.
        """
        try:
            self.product_list.delete(0, tk.END)
            for p in self.products:
                self.product_list.insert(tk.END, f"{p.name} - ₹{p.price}")
        except Exception:
            print("Loading products failed")

    def search_product(self):
        """
        Search product by keyword.
        """
        try:
            keyword = self.search_entry.get().lower()
            self.product_list.delete(0, tk.END)
            for p in self.products:
                if keyword in p.name.lower():
                    self.product_list.insert(tk.END, f"{p.name} - ₹{p.price}")
        except Exception:
            print("Product search failed")

    def add_to_cart(self):
        """
        Add selected product with quantity to cart.
        """
        try:
            selected = self.product_list.curselection()
            if not selected:
                messagebox.showwarning("Error", "Select product")
                return

            name = self.product_list.get(selected).split(" - ")[0]
            qty = int(self.qty_spin.get())

            self.cart.add_item(name, qty, self.username)
            messagebox.showinfo("Added", f"{qty} x {name} added")
            self.qty_spin.delete(0, tk.END)
            self.qty_spin.insert(0, "1")
        except Exception:
            print("Add to cart failed")
        
    def open_history(self):
        """
        Show purchase history of the user.
        """
        try:
            purchase_orders = self.order_manager.get_user_orders(self.username)
            history = ""
            for o in purchase_orders:
                history+=f"{o[4]}{' '*10}{o[1]} x{o[2]} = ₹{o[3]}\n"
            if not history:
                history = "No orders yet!"
            messagebox.showinfo("Order History", history)
        except Exception:
            print("View of purchase history failed")

    # ================= CART =================

    def create_cart_frame(self):
        """
        Create cart UI components.
        """
        try:
            self.cart_label = tk.Label(self.cart_frame, text="Your Cart",
                     font=("Arial", 25))
            self.cart_label.pack()

            self.cart_list = tk.Listbox(self.cart_frame)
            self.cart_list.pack(fill="both", expand=True)

            self.total_label = tk.Label(self.cart_frame, text="Total: ₹0")
            self.total_label.config(bg='lightgreen')
            self.total_label.pack()

            tk.Button(self.cart_frame, text="Pay",
                      command=self.pay, bg="lightblue", activebackground="red").pack(pady=5)

            tk.Button(self.cart_frame, text="Remove Item",
                      command=self.remove_selected_item).pack(pady=5)

            tk.Button(self.cart_frame, text="Back to User",
                      command=lambda: self.show_frame(self.user_frame)).pack(pady=5)
        except Exception:
            print("Cart frame creation failed")

    def open_cart(self):
        """
        Open cart and refresh display.
        """
        try:
            self.update_cart_display()
            self.cart_label.config(text=f"{self.username}'s Cart")
            self.show_frame(self.cart_frame)
        except Exception:
            print("Opening cart failed")

    def update_cart_display(self):
        """
        Update cart list and calculate total.
        """
        try:
            self.cart_list.delete(0, tk.END)
            total = 0

            for name, qty in self.cart.get_items(self.username).items():
                for p in self.products:
                    if p.name == name:
                        subtotal = p.price * qty
                        total += subtotal
                        self.cart_list.insert(
                            tk.END, f"{name} x {qty} = ₹{subtotal}"
                        )

            self.total_label.config(text=f"Total: ₹{total}")
        except Exception:
            print("Updating cart display failed")

    def remove_selected_item(self):
        """
        Remove selected item from cart.
        """
        try:
            selected = self.cart_list.curselection()
            if not selected:
                return

            item_text = self.cart_list.get(selected)
            name = item_text.split(" x ")[0]
            self.cart.remove_item(name, self.username)
            self.update_cart_display()
        except Exception:
            print("Removing cart item failed")

    def pay(self):
        """
        Process payment and save order.
        """
        try:
            if not self.cart.get_items(self.username):
                messagebox.showinfo("Cart", "Cart is empty")
                return

            total = 0
            for name, qty in self.cart.get_items(self.username).items():
                for p in self.products:
                    if p.name == name:
                        subtotal = p.price * qty
                        total += subtotal
                        self.order_manager.save_order(
                            self.username, name, qty, subtotal)

            messagebox.showinfo("Pay", f"Total Paid: ₹{total}")
            self.cart.clear_cart(self.username)
            self.update_cart_display()
            self.login_label.config(text=f"{self.username}'s Shopping Panel")
            self.show_frame(self.user_frame)
        except Exception:
            print("Payment processing failed")

    # ================= ADMIN =================

    def create_admin_frame(self):
        """
        Create admin dashboard UI.
        """
        try:
            tk.Label(self.admin_frame, text="Admin Panel",
                     font=("Arial", 25)).pack()

            tk.Label(self.admin_frame, text="All Products").pack()
            self.admin_products = tk.Listbox(self.admin_frame, height=15)
            self.admin_products.pack(fill="both", padx=10)

            tk.Label(self.admin_frame, text="User Orders").pack()
            self.admin_orders = tk.Listbox(self.admin_frame, height=15)
            self.admin_orders.pack(fill="both", padx=10)

            tk.Button(self.admin_frame, text='Most Purchased Product',
                      command=self.show_highest_product_purchase).pack(pady=5)

            tk.Button(self.admin_frame, text="Logout",
                      command=lambda: self.show_frame(self.login_frame)).pack(pady=5)
        except Exception:
            print("Admin frame creation failed")

    def load_admin_data(self):
        """
        Load product and order data into admin dashboard.
        """
        try:
            self.admin_products.delete(0, tk.END)
            self.admin_orders.delete(0, tk.END)

            for p in self.products:
                self.admin_products.insert(
                    tk.END, f"{p.name} - ₹{p.price}"
                )

            for o in self.order_manager.get_orders():
                self.admin_orders.insert(
                    tk.END, f"{o[4]}{' '*10}{o[0]} bought {o[1]} x{o[2]} = ₹{o[3]}"
                )
        except Exception:
            print("Loading admin data failed")

    def show_highest_product_purchase(self):
        """
        Display most frequently purchased product.
        """
        try:
            product_names = [i[1] for i in self.order_manager.get_orders()]

            result = "No Purchases yet!"
            counter = Counter(product_names)

            if len(counter.values()) > 0:
                max_count = max(counter.values())
                result = ",".join([k for k, v in counter.items() if v == max_count])

            messagebox.showinfo("Most Purchased", result)
        except Exception:
            print("Calculating highest purchased product failed")          
            
            