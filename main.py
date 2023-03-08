#------------------------------------DZ_5--------------------------------

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# def recurs(a, b):
#     if b == 0:
#         return 1
#     return recurs(a, b - 1) * a

# n = int(input("Введите число a: "))
# m = int(input("Введите число b: "))
# print(recurs(n, m)) 

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def RecurSum(a, b):
    if b == 0:
        return a
    return RecurSum(a, b - 1) + 1

n = int(input("Введите число a: "))
m = int(input("Введите число b: "))
print(RecurSum(n, m)) 
