
#while_loop to average exam scores for each student

count = 0

answer = input("Do you want to enter a student? (Yes/No): ")

while answer == "yes":
    last_name = input("Enter last name: ")
    first_exam = int(input("Enter first exam score: "))
    second_exam = int(input("Enter second exam score: "))

    average = (first_exam + second_exam) / 2
    print(f"{last_name}'s average score is {average}")

    count += 1

    answer = input("Do you want to enter another student? (Yes/No): ")

print(f"Number of students entered: ({count})")



    

    