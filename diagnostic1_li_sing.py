def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping_cost = 15
    elif shipping_speed == "standard":
        shipping_cost = 5
    elif shipping_speed == "overnight":
        shipping_cost = 25
    elif shipping_speed == "standard" and cart_total >= 100:
        return cart_total + 0  
    else:
        shipping_cost = 0
    return cart_total + shipping_cost

print(calculate_checkout(cart_total = 5, shipping_speed = "express"))  # Expected output: 95
print(calculate_checkout(cart_total = 120, shipping_speed = "standard"))  # Expected output: 120
print(calculate_checkout(cart_total = 120, shipping_speed = "express"))  # Expected output: 135
print(calculate_checkout(cart_total = 120, shipping_speed = "overnight"))  # Expected output: 145


