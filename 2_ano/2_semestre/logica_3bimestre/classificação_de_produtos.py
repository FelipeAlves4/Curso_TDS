class Product:
    def __init__(self, price, category):
        self.price = price
        self.category = category

def classify_product(product):
    if product.category == "luxo" and product.price > 1000:
        return "Premium"
    elif product.category == "moda" and product.price < 500:
        return "Acessível"
    elif product.category == "eletrônicos" and product.price > 500:
        return "Padrão"
    else:
        return "Não classificado"


preço= int(input("Qual o valor do produto? "))
categoria = input("Qual a categoria do produto? ")

product1 = Product(preço, categoria)
print(classify_product(product1))  # Saída: Premium
preço = int(input("Qual o preço do produto? "))
categoria = input("Qual a categoria do produto? ")

product2 = Product(preço, categoria)
print(classify_product(product2))  # Saída: Acessível

preço = int(input("Qual o preço do produto? "))
categoria = input("Qual a categoria do produto? ")

product3 = Product(preço, categoria)
print(classify_product(product3))  # Saída: Padrão