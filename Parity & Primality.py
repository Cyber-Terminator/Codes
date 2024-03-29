num = int(input("Enter your number: "))

if num % 2 == 0:
    parity = "Even"    

else:
    parity = "Odd"

if num == 1:
    primality = "Composite"
else:
    for i in range(2, num):
        if num % i == 0:
            primality = "Composite"
            break
    else:
        primality = "Prime"

print("\n------------------")
print(f"{num}\n{parity}\n{primality}")
print("------------------")
