
def get_pay_rate(job_code):
    if job_code == "L":
        return 25
    elif job_code == "A":
        return 30
    elif job_code == "J":
        return 50
    else:
        return 0


total_gross_pay = 0

response = input("Do you want to enter an employee? (Yes/No): ")

while response.lower() == "yes":
    last_name = input("Enter last name: ")
    job_code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))

    rate = get_pay_rate(job_code)

    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate

    total_gross_pay = total_gross_pay + gross_pay

    print("Last Name:", last_name)
    print("Gross Pay: $", format(gross_pay, ",.2f"))
    print()

    response = input("Do you want to enter another employee? (Yes/No): ")

print()
print("Total Gross Pay: $", format(total_gross_pay, ",.2f"))