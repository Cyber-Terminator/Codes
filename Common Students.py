num_statistics = int(input(print("How many statistics students are there? ")))
if num_statistics > 0:
    input(print("Enter statistics student name: "))
    num_statistics -= 1


all_departments = statistics & maths & computer
statistics_math = statistics & math
statistics_computer = statistics & computer
math_computer = math & computer

if all_departments:
    print("Students with the same name in all three departments:")
    print(all_departments)
elif statistics_math:
    print("Students with the same name in statistics and math:")
    print(statistics_math)
elif statistics_computer:
    print("Students with the same name in statistics and computer:")
    print(statistics_computer)
elif math_computer:
    print("Students with the same name in statistics and math:")
    print(math_computer)
else:
    print("No students found with the same name in all three departments.")
