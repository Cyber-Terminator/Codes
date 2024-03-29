while True:
    
    print("""
0 = End Program
1 = Addition
2 = Subtraction
3 = Multiplication
4 = Division""")
    print()
    
    op = int(input("What operation would you like to do? "))
    print()

    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))
    print()
    if op == 0:
        break
    if op == 1:
        out = num_1 + num_2
        print("The answer is " + str(out))
    if op == 2:
        out = num_1 - num_2
        print("The answer is " + str(out))
    if op == 3:
        out = num_1 * num_2
        print("The answer is " + str(out))
    if op == 4:
        out = num_1 / num_2
        print("The answer is " + str(out))

    else:
        print("Please enter a valid operation.")
        print()
        
    print()
    
