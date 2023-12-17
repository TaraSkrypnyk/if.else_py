try:
    a = -1
    dig = 3
    low = 3
    upp = 3
    sign = 3
    while a <= 0:
        a = int(input("Введіть довжину пароля "))
    while dig < 0 or dig>1:
        dig = float(input("Якщо ви хочете щоб в вашому паролі були цифри натисніть 1, інакше натисніть 0 "))
    while low < 0 or low > 1:
        low = float(input("Якщо ви хочете щоб в вашому паролі були маленькі літери натисніть 1, інакше натисніть 0 "))
    while upp < 0 or upp > 1:
        upp = float(input("Якщо ви хочете щоб в вашому паролі були еликі літери натисніть 1, інакше натисніть 0 "))
    while sign < 0 or sign > 1:
        sign = float(input("Якщо ви хочете щоб в вашому паролі були пеціальні символи 1, інакше натисніть 0 "))

    import random
    dig_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    upp_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    low_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sign_list= ['@', '#', ',', '?', '*', '.', '%']
    print("Вибір випадкової великої літери - ", random.choice(upp_list))
    print("Вибір випадкової маленької літери - ", random.choice(low_list))
    # if a > b:
    #     a, b = b, a
    # for i in range(a, b):
    #     if a % 7 == 0:
    #         print(a)
    #     # a += 1
except Exception as e:
    print(e)