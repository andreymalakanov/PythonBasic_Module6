# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк:
# ему приносят такие большие счета, что числа не помещаются на бумаге.
 
# Напишите программу,
# которая считала бы для него,
# сколько десятичных цифр (знаков) во вводимом числе.

num = int(input('Введите число: '))
num_count = 0
while num != 0:
  num_count += 1
  num = num // 10
print('Десятичных цифр (знаков) во вводимом числе:', num_count)