# Andrey Malakanov
# Skillbox PythonBasic

print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

X = int(input('Введите сумму вклада: '))
P = int(input('Введите годовой процент по вкладу: '))
Y = int(input('Введите ожидаемую сумму вклада: '))
year_count = 0
while X < Y:
  year_count += 1
  X += int((X * P) / 100)
#  print(year_count, X)
if (year_count % 10 > 4) or (year_count % 10 == 0) or (year_count % 100 > 10 and year_count % 100 < 20):
  year_name = 'лет'
elif year_count % 10 == 1:
  year_name = 'год'
else:
  year_name = 'года'
print(f'Для достижения значения {Y} на банковском счете, потребуется {year_count} {year_name}')