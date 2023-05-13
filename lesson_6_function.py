def calculate_price ( quantity, price):
    total_price = quantity * price 
    discount =  0.1

    def apply_discount (price):
        return price * (1 - discount)
    
    return apply_discount (total_price)

result =  calculate_price (5, 10)
print (result)
# Global scope and local scope in Python refers to the visibility of variables. If a variable is defined in the global scope, 
# it's accessible from anywhere in the code. But if it's defined within a function (local scope), it can only be used within that function.