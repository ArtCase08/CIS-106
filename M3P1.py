# INPUT
ticker = input("Stock ticker symbol: ")
shares = int(input("Enter amount of shares: "))
cost = float(input("Enter cost per share: "))

# PROCESSING
amount_invested = shares * cost

# OUTPUT
print("Stock:", ticker)
print(f"Amount invested: ${amount_invested:}")
