f = open("students.txt", "r")

total_tuition = 0.0   # sum of all tuition owed
count = 0             # number of students

print(f"{'Last Name':<12}{'Credits':>9}{'Tuition':>14}")

lastname = f.readline().rstrip('\n')        # prime read

while lastname != "":
    district = f.readline().rstrip('\n')
    credits = float(f.readline())

    if district == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    tuition = credits * cost_per_credit
    total_tuition = total_tuition + tuition
    count = count + 1

    print(f"{lastname:<12}{credits:>9.0f}{'$' + format(tuition, ',.2f'):>14}")

    lastname = f.readline().rstrip('\n')    # read next

f.close()

print()
print("Total tuition owed: $" + format(total_tuition, ",.2f"))
print("Number of students:", count)
