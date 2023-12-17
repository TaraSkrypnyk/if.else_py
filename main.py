try:
    a = int(1)
    b = -1
    while b <= 0:
        b = int(input("Введіть число "))
    s = str(input("Введіть символ "))
    for i in range(a, b + 1):
        print(s, end='')
        a += 1
except Exception as e:
    print(e)