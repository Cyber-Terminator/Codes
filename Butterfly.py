
for i in range(7, -1, -1):
    for j in range(14):
        if j < 7 - i or j >= 7 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, 7):
    for j in range(14):
        if j < 7 - i or j >= 7 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

