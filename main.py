try:
    import random

    symbol_list = [0, 1, 2, 3]
    dig_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    upp_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    low_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    sign_list = ['@', '#', ',', '?', '*', '.', '%']
    dig = 3
    low = 3
    upp = 3
    sign = 3
    b =-1
    password=str()
    while b <= 0:
        b = int(input("Введіть довжину пароля "))
    while dig < 0 or dig>1:
        dig = float(input("Якщо ви хочете щоб в вашому паролі були цифри натисніть 1, інакше натисніть 0 "))
    while low < 0 or low > 1:
        low = float(input("Якщо ви хочете щоб в вашому паролі були маленькі літери натисніть 1, інакше натисніть 0 "))
    while upp < 0 or upp > 1:
        upp = float(input("Якщо ви хочете щоб в вашому паролі були еликі літери натисніть 1, інакше натисніть 0 "))
    while sign < 0 or sign > 1:
        sign = float(input("Якщо ви хочете щоб в вашому паролі були пеціальні символи 1, інакше натисніть 0 "))
    while (len(password)<b):
        r = random.choice(symbol_list)
        if r==0:
            if dig==1:
                d = random.choice(dig_list)
                password += d
        elif r==1:
            if low==1:
                l = random.choice(low_list)
                password += l
        elif r==2:
            if upp==1:
                u = random.choice(upp_list)
                password += u
        elif r==3:
            if sign==1:
                s = random.choice(sign_list)
                password += s
    print("Ваш пароль: " + str(password))
except Exception as e:
    print(e)