# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток,
# которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет,
# которые нужно перевернуть

N=int(input("Введите кол-во монеток:"))
print("Введите положение монеток 0 - решка 1 - герб")
x=0
y=0
fl=0
for i in range(0,N):
    k=int(input())
    if k==0:
        x+=1
    elif k==1:
        y+=1
    else:
        print("Ошибка ввода")
        fl=-1
        break
if fl==0:
    if x<y:
        print(f"Наименьшее количество переворачиваний {x}")
    else:
        print(f"Наименьшее количество переворачиваний {y}")
    

# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

S=int(input("Введите сумму чисел:"))
P=int(input("Введите произведение чисел:"))
for i in range(0,S):
    if i*(S-i)==P:
        print(f"Нужные числа {i} и {S-i}")
        break


# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.


N=int(input("Введите максимальное значение:"))
i=0
while pow(2,i)<=N:
    print(pow(2,i), end=" ")
    i+=1


# 