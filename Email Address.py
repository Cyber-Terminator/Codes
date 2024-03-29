email = input("Enter an email address: ")

x = email.find("@" and ".")

if x > 0:
    print("Valid email address.")
else:
    print("Invalid email address.")
