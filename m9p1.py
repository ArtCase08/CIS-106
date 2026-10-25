
def compute_ext_price(qty, unit_price):
    ext_price = qty * unit_price
    if ext_price > 10000.00:
        ext_price = ext_price * 0.90   
    return ext_price


total_ext_price = 0

response = input("Do you want to enter an item? (Yes/No): ")

while response.lower() == "yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    ext_price = compute_ext_price(qty, price)
    total_ext_price = total_ext_price + ext_price

    print("Quantity:", qty)
    print("Price: $", format(price, ",.2f"))
    print("Extended Price: $", format(ext_price, ",.2f"))
    print()

    response = input("Do you want to enter another item? (Yes/No): ")

print()
print("Total Extended Price: $", format(total_ext_price, ",.2f"))