# Задача номер 1
import math

phrase1 = input()
phrase2 = input()
if len(phrase2) > len(phrase1):
    print('Фраза 2 длинее фразы 1')
elif len(phrase1) > len(phrase2):
    print('Фраза 1 длинее фразы 2')
else:
    print('Они равны')

# Задача номер 2
userYear = input()
if int(userYear) % 4 == 0:
    print('год високосный')
else:
    print('год невесокосный')

# Задача номер 3
print('Введите ваш день рождения: ')
userDay = input()
print('Введите месяц рождения: ')
userMounth = input()
if ((int(userDay) >= 21) and (userMounth == 'Март')) or ((int(userDay) <= 19) and (userMounth == 'Апрель')):
    print('Овен')
elif ((int(userDay) >= 20) and (userMounth == 'Апрель')) or ((int(userDay) <= 20) and (userMounth == 'Май')):
    print('Телец')
elif ((int(userDay) >= 21) and (userMounth == 'Май')) or ((int(userDay) <= 21) and (userMounth == 'Июнь')):
    print('Близнецы')
elif ((int(userDay) >= 22) and (userMounth == 'Июнь')) or ((int(userDay) <= 22) and (userMounth == 'Июль')):
    print('Рак')
elif ((int(userDay) >= 23) and (userMounth == 'Июль')) or ((int(userDay) <= 22) and (userMounth == 'Август')):
    print('Лев')
elif ((int(userDay) >= 23) and (userMounth == 'Август')) or ((int(userDay) <= 22) and (userMounth == 'Сентябрь')):
    print('Дева')
elif ((int(userDay) >= 23) and (userMounth == 'Сентябрь')) or ((int(userDay) <= 23) and (userMounth == 'Октябрь')):
    print('Весы')
elif ((int(userDay) >= 24) and (userMounth == 'Октябрь')) or ((int(userDay) <= 22) and (userMounth == 'Ноябрь')):
    print('Скорпион')
elif ((int(userDay) >= 23) and (userMounth == 'Ноябрь')) or ((int(userDay) <= 21) and (userMounth == 'Декабрь')):
    print('Стрелец')
elif ((int(userDay) >= 22) and (userMounth == 'Декабрь')) or ((int(userDay) <= 20) and (userMounth == 'Январь')):
    print('Козерог')
elif ((int(userDay) >= 21) and (userMounth == 'Январь')) or ((int(userDay) <= 18) and (userMounth == 'Февраль')):
    print('Водолей')
elif ((int(userDay) >= 19) and (userMounth == 'Февраль')) or ((int(userDay) <= 20) and (userMounth == 'Март')):
    print('Рыбы')

# Задача номер 4
userInputWeight = input()
userInputHeight = input()
userInputLength = input()
if (int(userInputWeight) <= 15) and (int(userInputHeight) <= 15) and (int(userInputLength) <= 15):
    print('Коробка 1')
elif (int(userInputWeight) > 200) or (int(userInputHeight) > 200) or (int(userInputLength) > 200):
    print('Коробка для лыж')
elif ((int(userInputWeight) >
       15) and (int(userInputWeight) < 50)) or ((int(userInputHeight) >
                                                 15) and (int(userInputHeight) < 50)) or ((int(userInputLength) >
                                                                                           15) and (int(userInputLength)
                                                                                                    < 50)):
    print('Коробка 2')
else:
    print('Коробка 3')

    # Задача номер 5
print('Введите 6-ти значное число')
userNumber = input()
if (int(userNumber[0])+ int(userNumber[1]) + int(userNumber[2]) == int(userNumber[3])+ int(userNumber[4]) +
        int(userNumber[5])):
    print('Счастливый билетик')
else:
    print('Несчастливый')

# Задача номер 4
userFigure = input()
if userFigure == 'Круг':
    print('Введите радус')
    R = input()
    print(int(R) * math.pi)
elif userFigure == 'Треугольник':
    print('Введите сторону A')
    A = input()
    print('Введите сторону B')
    B = input()
    print('Введите сторону C')
    C = input()
    P = (int(A) + int(B) + int(C))/2
    print(math.sqrt(P * (P-int(A)) * (P-int(B)) * (P-int(C))))
else:
    print('Введите сторону A')
    A = input()
    print('Введите сторону B')
    B = input()
    print(int(A)*int(B))