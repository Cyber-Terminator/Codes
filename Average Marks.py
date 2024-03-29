num_students = 60

name = str(input("Enter Student Name: "))


math = int(input("Enter Marks in Math: "))
science = int(input("Enter Marks in Science: "))
english = int(input("Enter Marks in English: "))
history = int(input("Enter Marks in History: "))
pe = int(input("Enter Marks in PE: "))

score = math + science + english + history + pe
average = score / 5

print(name + "'s average is " + str(average))
