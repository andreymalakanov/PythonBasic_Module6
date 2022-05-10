# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 4. Календари')

# Ваня увлекается историей, а в особенности календарями.
# Он изучает календари разных времён, эпох и народностей. 
# Для исследования ему нужно посчитать,
# у кого сколько было месяцев с чётным количеством дней.
 
# Напишите программу,
# которая считает количество только чётных чисел в последовательности 
# (последовательность заканчивается при вводе нуля)
# и выводит ответ на экран.

mounths = int(input('Введите колличество месяцев: '))
mounths_counter = 0
mounths_even_counter = 0
while mounths_counter != mounths:
  mounths_counter += 1
  day_in_mounth = int(input(f'Введите количество дней в месяце {mounths_counter} из {mounths}. '))
  mounths_even = day_in_mounth % 2
  if mounths_even == 0:
    mounths_even_counter += 1
print('Колличество месяцев с четными днями =', mounths_even_counter)