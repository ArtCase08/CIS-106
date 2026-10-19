principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))

year = 1               
total_interest = 0.0    
print()
print(f"{'Year':<6}{'Beginning':>14}{'Ending':>14}")
print(f"{'':<6}{'Balance':>14}{'Balance':>14}")

while year <= 5:
    interest = principal * rate
    ending = principal + interest
    total_interest = total_interest + interest
    print(f"{year:<6}{'$' + format(principal, ',.2f'):>14}{'$' + format(ending, ',.2f'):>14}")
    principal = ending       
    year = year + 1          

print()
print("Total interest earned: $" + format(total_interest, ",.2f"))