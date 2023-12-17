try:
    a = int(input("Введіть початок діапазону "))
    b = int(input("Введіть і діапазону "))
    c = float(0)
    d = float(0)
    f = a
    if a > b:
        a, b = b, a
    for i in range(a, b):
        c += a
        a += 1
    print("Сума дорівнює " + str(c) )
    d=c/(b-f)
    print("Середнє арефметичне дорівнює " + str(d))
except Exception as e:
    print(e)