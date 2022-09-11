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
