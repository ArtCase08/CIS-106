#input
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
msrp = float(input("Enter the retail price of the car: "))
discount_percent = float(input("Enter the discount rate as a decimal: "))


#processing
discount_amount = msrp * discount_percent
discounted_price = msrp - discount_amount

#output
print("The make is", make)
print("The model is", model)
print(f"the price is ${msrp:}")
print("The discount rate is", discount_percent)
print(f"The amount off is ${discount_amount:}")
print(f"The final price including discount price is ${discounted_price:}")
