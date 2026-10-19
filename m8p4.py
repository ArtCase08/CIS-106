f = open("orders.txt", "r")

total = 0.0     # sum of extended prices
count = 0       # number of orders

print(f"{'Item':<14}{'Qty':>6}{'Price':>12}{'Ext. Price':>14}")

item = f.readline().rstrip('\n')      # prime read

while item != "":
    qty = float(f.readline())
    price = float(f.readline())

    ext_price = qty * price
    total = total + ext_price
    count = count + 1

    print(f"{item:<14}{qty:>6.0f}{'$' + format(price, ',.2f'):>12}{'$' + format(ext_price, ',.2f'):>14}")

    item = f.readline().rstrip('\n')  # read next item

f.close()

avg = total / count

print()
print("Total of extended prices: $" + format(total, ",.2f"))
print("Number of orders:         ", count)
print("Average order:            $" + format(avg, ",.2f"))
