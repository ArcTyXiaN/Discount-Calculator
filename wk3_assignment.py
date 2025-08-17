def calculate_discount(price, discount):
    discount_rate = discount /100
    if discount >=20:
        discounted_price = price - (discount_rate * price)
        return discounted_price
    else:
        return price
    #inputs
price = float(input("Enter Price"))
#loop, try and except to avoid error
while True:
    try:
        discount = float(input("Enter Discount Percentage"))
        break
    except ValueError:
        print("Please enter a valid number")
final_price = calculate_discount(price, discount)
print(f"Pay {final_price} after {discount}% discount")
