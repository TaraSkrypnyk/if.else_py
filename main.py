try:
    a = int(1)
    res = str()
    b = -1
    while b <= 0:
        b = int(input("Введіть число "))
    s = str(input("Введіть символ "))
    for i in range(a, b + 1):
        res += (s)
        a += 1
    print(res)
except Exception as e:
    print(e)