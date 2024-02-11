from ecomproduct import Product

#Creating our products
product1 = Product("01", "OLED Monitor", "Electronics", 499.99, 25, 4.7)
product2 = Product("02", "VR Headset", "Eletronics", 999.99, 10, 4.2)
product3 = Product("03", "Laptop", "Electronics", 1099.99, 50, 4.8)
product4 = Product("04", "Mechanical Keyboard", "Electronics", 199.99, 70, 4.1)

#Shows the product details
print(product1)
print(product2)
print(product3)
print(product4)

#Update some details for products
product1.update_stock(10)
product2.update_stock(15)
product3.change_price(1799.99)

#Shows the updated details
print(product1)
print(product2)
print(product3)
