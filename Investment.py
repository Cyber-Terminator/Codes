p = int(input("Enter the Principal amount (in rupees): "))
r = int(input("Enter the Rate of Interest (per year): "))
t = int(input("Enter the Number of Years: "))

si = (p * r * t) / 100
ci = p * (1 + (r / 100)) ** t - p

print("Simple Interest: Rs. " + str(si))
print("Compound Interest: Rs. " + str(ci))
