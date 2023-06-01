#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
N = int(input("Введите кол-во элементов: "))
A = []
for i in range(N):
    z = int(input(f"Введите {i+1}ое число: "))
    A.append(z)
X = int(input("Ближайшее к какому значению ищем? "))
for i in range(N):
    minimalnoe = abs(X - A[0])
    index = 0
    for i in range(1, N):
        raznitsa = abs(X - A[i])
        if raznitsa < minimalnoe:
            minimalnoe = raznitsa
            index = i
print(A[index])
