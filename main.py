# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = 0
while num < 1 or num > 7:
    print("Введите день недели:")
    num = int(input())
    if num < 1 or num > 7:
        print("Повторите ввод. Необходимо число от 1 до 7!")
if num == 6 or num == 7:
    print("да")
else:
    print("нет")

# 2 Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
flag = True
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (x or y or z) != (not x and not y and not z):
                flag = False
                break
        if not flag:
            break
    if not flag:
        break
if flag:
    print("истина")
else:
    print("ложь")

# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("Введите x: ")
x = int(input())
print("Введите y: ")
y = int(input())
if y > 0:
    if x > 0:
        print(1)
    else:
        print(2)
else:
    if x < 0:
        print(3)
    else:
        print(4)

