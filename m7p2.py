#while_loop to count from a start value to a stop value by an increment

start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
increment = int(input("Enter the increment value: "))

number = start
while number <= stop:
    print(number)
    number += increment
