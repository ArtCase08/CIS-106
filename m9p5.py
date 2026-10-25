
def compute_tuition(credit_hours, district_code):
    if district_code == "I":
        return credit_hours * 250
    elif district_code == "O":
        return credit_hours * 550
    else:
        return 0


total_tuition = 0

response = input("Do you want to enter a student? (Yes/No): ")

while response.lower() == "yes":
    last_name = input("Enter student last name: ")
    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter district code (I or O): ").upper()

    tuition = compute_tuition(credit_hours, district_code)
    total_tuition = total_tuition + tuition

    print("Student:", last_name)
    print("Tuition Owed: $", format(tuition, ",.2f"))
    print()

    response = input("Do you want to enter another student? (Yes/No): ")

print()
print("Total Tuition Owed: $", format(total_tuition, ",.2f"))