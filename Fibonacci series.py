while True:
    number = int(input("What number of the Fibonacci series do you want to know? "))

    loop = 0
    pre_series = 1
    series = 0

    while loop < number:
        series, pre_series = pre_series, series + pre_series
        loop += 1

    print(series)
