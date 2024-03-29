x = 0
y = 1

for i in range(10):
    print()
    x += 1
    y = 1
    for j in range(10):
        print(x * y, end=' ')
        y += 1
