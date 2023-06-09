#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
#Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
#Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
#Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
#Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def rifma(fraza):
    count_glasnih = list()
    words = fraza.split()
    glasnie = ["а", "о", "э", "е", "и", "ы", "у", "ё", "ю", "я"]
    for word in words:
        count = 0
        for symbol in word:
            if symbol in glasnie:
                count += 1
        count_glasnih.append(count)
    if len(set(count_glasnih)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")


fraza = input("Что сказал Вини?: ")
rifma(fraza)