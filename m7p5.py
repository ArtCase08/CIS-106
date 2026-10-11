#while_loop to compute discounts on orders

total_discount = 0

answer = input("Do you want to enter an order? (Yes/No): ")

while answer.lower() == "yes":
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price of item: "))

    extended_price = quantity * price

    if extended_price > 10000.00:
        discount_percent = 0.25
    else:
        discount_percent = 0.10

    discount_amount = extended_price * discount_percent
    total = extended_price - discount_amount

    print(f"Extended price: ${extended_price:.2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")

    total_discount += discount_amount

    answer = input("Do you want to enter another order? (Yes/No): ")

print(f"Sum of all discounts: ${total_discount:.2f}")