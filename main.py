try:
    a = int(input("Введіть початок діапазону "))
    b = int(input("Введіть і діапазону "))
    if a > b:
        a, b = b, a
    for i in range(a, b):
        if a % 15 == 0:
            print("Fizz Buzz")
        elif a % 5 == 0:
            print("Buzz")
        elif a % 3 == 0:
            print("Fizz")
        else:
            print (a)
        a += 1
except Exception as e:
    print(e)