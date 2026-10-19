
f = open("employees.txt", "r")

total_bonus = 0.0

print(f"{'Last Name':<12}{'Salary':>14}{'Bonus':>12}")

lastname = f.readline().rstrip('\n')      

while lastname != "":
    salary = float(f.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus = total_bonus + bonus

    print(f"{lastname:<12}{'$' + format(salary, ',.2f'):>14}{'$' + format(bonus, ',.2f'):>12}")

    lastname = f.readline().rstrip('\n') 

f.close()

print()
print("Total bonuses paid: $" + format(total_bonus, ",.2f"))