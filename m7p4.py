#while_loop to compute gross pay for each employee

total_pay = 0
count = 0

answer = input("Do you want to enter employee? (Yes/No): ")

while answer == "yes":
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))

    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate

    print(f"{last_name}'s gross pay is ${gross_pay:.2f}")

    total_pay += gross_pay
    count += 1

    answer = input("Do you want to enter another employee? (Yes/No): ")

print(f"Total gross pay: ${total_pay:.2f}")
print(f"Number of employees: {count}")

if count > 0:
    average_pay = total_pay / count
    print(f"Average pay: ${average_pay:.2f}")