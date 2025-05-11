class EcommerceSystem:
    def __init__(self):
        self.users = []
        self.products = []
        self.orders = []

    def add_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def place_order(self, user, product):
        if product in self.products:
            self.orders.append((user, product))
            return "Order placed successfully"
        return "Product not available"

# Exemplo de uso
system = EcommerceSystem()
system.add_user("Alice")
system.add_product("Laptop")
print(system.place_order("Alice", "Laptop"))
system.add_user("Felipe")
system.add_product("pc")
print(system.place_order("Felipe", "pc"))


