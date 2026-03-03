from datetime import datetime

class Product:
    """
    Represents a product with a name and price.
    """
    def __init__(self, name, price):
        """
        Initializes a Product object.

        Args:
            name (str): Name of the product.
            price (int or float): Price of the product.
        """
        self.name = name
        self.price = price


class Cart:
    """
    Manages cart items for multiple users.
    Stores items in format:
    {
        username: {
            product_name: quantity
        }
    }
    """
    def __init__(self):
        """Initialize an empty cart dictionary."""
        self.items = {}

    def add_item(self, product_name, quantity, username):
        """
        Adds a product with quantity to a user's cart.

        Args:
            product_name (str): Name of product.
            quantity (int): Quantity to add.
            username (str): Username of the customer.
        """
        try:
            if username not in self.items:
                self.items[username] = {}

            if product_name in self.items[username]:
                self.items[username][product_name] += quantity
            else:
                self.items[username][product_name] = quantity
        except Exception as e:
            print(f"Error adding item to cart: {e}")
            
    def remove_item(self, product_name, username):
        """
        Removes a product from the user's cart.

        Args:
            product_name (str): Name of product.
            username (str): Username of the customer.
        """
        """
        Removes a product from the user's cart.

        Args:
            product_name (str): Name of product.
            username (str): Username of the customer.
        """
        try:
            if product_name in self.items[username]:
                del self.items[username][product_name]
        except Exception as e:
            print(f"Error removing item from cart: {e}")

    def clear_cart(self, username):
        """
        Clears all items for a given user.

        Args:
            username (str): Username of the customer.
        """
        try:
            self.items[username] = {}
        except Exception as e:
            print(f"Error clearing cart: {e}")

    def get_items(self, username):
        """
        Returns all items in a user's cart.

        Args:
            username (str): Username of the customer.

        Returns:
            dict: Dictionary of products and quantities.
        """
        try:
            if not self.items.get(username):
                self.items[username] = {}
            return self.items.get(username)
        except Exception as e:
            print(f"Error retrieving cart items: {e}")


class OrderManager:
    """
    Manages order history in memory.
    Stores orders as tuples:
    (username, product_name, quantity, total, timestamp)
    """
    def __init__(self):
        """
        Initializes empty order storage.
        """
        self.orders = []  # Store order history in memory

    def save_order(self, username, product_name, quantity, total):
        """
        Saves an order record.

        Args:
            username (str): Username of customer.
            product_name (str): Product name.
            quantity (int): Quantity ordered.
            total (float): Total price.
        """
        try:
            self.orders.append((username, product_name, quantity, total, str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))))
        except Exception as e:
            print(f"Error saving order: {e}")

    def get_orders(self):
        """
        Returns all orders.

        Returns:
            list: List of all order records.
        """
        try:
            return self.orders
        except Exception as e:
            print(f"Error retrieving orders: {e}")
    
    def get_user_orders(self, username):
        """
        Returns orders for a specific user.

        Args:
            username (str): Username of customer.

        Returns:
            list: List of user's orders.
        """
        try:
            return [i for i in self.orders if i[0] == username]
        except Exception as e:
            print(f"Error retrieving user orders: {e}")