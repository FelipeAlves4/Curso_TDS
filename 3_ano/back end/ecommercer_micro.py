class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def check_availability(self, product):
        return product in self.products

class OrderService:
    def __init__(self):
        self.orders = []

    def place_order(self, user, product, product_service):
        if product_service.check_availability(product):
            self.orders.append((user, product))
            return "Order placed successfully"
        return "Product not available"

# Exemplo de uso com microsserviços
user_service = UserService()
product_service = ProductService()
order_service = OrderService()

user_service.add_user("Alice")
product_service.add_product("Laptop")
print(order_service.place_order("Alice", "Laptop", product_service))
