#Input
lastname = input("Enter your last name: ")
midterm = int(input("Enter midterm exam score: "))
final_exam = int(input("Enter final exam score: "))

#Processing
total_score = midterm * 0.4 + final_exam * 0.6

#Output
print("Student:", lastname)
print("Total Score:", total_score)
