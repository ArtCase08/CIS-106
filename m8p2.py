a = 1    # first number
b = 1    # second number

for i in range(1, 21):
    print(i, a)
    next_num = a + b    
    a = b               
    b = next_num