try:
    a= int(input("Введіть початок діапазону "))
    b = int(input("Введіть і діапазону "))
    if a>b:
        a,b=b,a
    for i in range(a,b):
        if a%7==0:
            print(a)
        a+=1

except Exception as e:
    print(e)
