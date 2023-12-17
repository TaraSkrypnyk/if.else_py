try:
    c = int(input("Введіть початок діапазону "))
    d = int(input("Введіть і діапазону "))
    a = c
    b = d
    if a > b:
        a, b = b, a
    print("Всі числа вашого діапазону")
    for i in range(a, b):
        print(a)
        a += 1
    a = c
    print("Всі числа вашого діапазону в зворотньому порядку")
    for i in range(a, b):
        b -= 1
        print(b)
    b = d
    print("Числа кратні 7")
    for i in range(a, b):
        if a % 7 == 0:
            print(a)
        a += 1
    a = c
    print("Числа кратні 5")
    for i in range(a, b):
        if a % 5 == 0:
            print(a)
        a += 1
except Exception as e:
    print(e)