income = int(input(print("What is your annual income? ")))
tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 5
elif income <= 750000:
    tax = 10
elif income <= 1000000:
    tax = 15
elif income <= 1250000:
    tax = 20
elif income <= 1500000:
    tax = 25
elif income > 1500000:
    tax = 30

tax_percent = tax / 100

print("You need to pay " + str(tax_percent * income))
