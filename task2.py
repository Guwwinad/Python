#Найдите сумму цифр трехзначного числа.

n=int(input("Введите 3-значное число: "))
if n > 999 or n < 100:
    print("Введите 3-значное число!!!: ")
print(f"{(n%10)+((n//10)%10)+(n//100)} = {n//100} + {(n//10)%10} + {n%10}")