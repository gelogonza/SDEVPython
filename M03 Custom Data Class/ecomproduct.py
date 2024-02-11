# E-commerce Product Class

class Product:
    def __init__(self, product_id, name, category, price, stock, rating=0):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = price
        self.__stock = stock
        self.__rating = rating
        
    #Getters and Setters
    def get_product_id(self):
        return self.__product_id
    
    def set_product_id(self, product_id):
        self.__product_id = product_id
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        self.__category = category
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price
        
    def get_stock(self):
        return self.__stock
    
    def set_stock(self, stock):
        self.__stock = stock
        
    def get_rating(self):
        return self.__rating
    
    def set_rating(self, rating):
        self.__rating = rating
        
    def update_stock(self, amount):
        if amount >= 0:
            self.__stock += amount
        else:
            print("Unvalid: Amount to update must be positive.")
            
    def change_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Error: Updated price must be positive.")
            
    def __str__(self):
        return (f"Product ID: {self.__product_id}, Name: {self.__name}, Category: {self.__category}, "
                f"Price: ${self.__price}, Stock: {self.__stock}, Rating: {self.__rating} stars")

    def __eq__(self, other):
        return self.__product_id == other.__product_id
    
