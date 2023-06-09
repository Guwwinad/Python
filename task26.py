#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def step(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return step(a, b - 1) * a


a = int(input("Введите число: "))
b = int(input("В какую степень возвести? "))

print(step(a, b))