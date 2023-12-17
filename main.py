try:
    a = int(1)
    res = int(1)
    b = -1
    while b<0:
        b = int(input("Введіть число "))
    if b==0:
        print("Факторіал вашого числа дорівнює 1")
    else:
         for i in range(a, b+1):
             res *= a
             a += 1
         print ("Факторіал вашого числа дорівнює " + str(res))
except Exception as e:
    print(e)