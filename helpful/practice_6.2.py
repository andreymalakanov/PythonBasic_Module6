# Andrey Malakanov
# Skillbox PythonBasic

# Practice 6.2 - 1 

summ = 0
number = int(input('Введите число: '))
while number != 0:
 summ += number
 number = int(input('Введите число: '))
print(summ)

# Practice 6.2 - 2

password = input('Введите пароль: ')
while password != '235':
 print('Введен не верный пароль!')
 password = input('Введите пароль еще раз: ')
print('Добро пожаловать!')

# Practice 6.2 - 3

balance = 0
while balance < 500000:
  save = int(input('Сколько денег следует отложить: '))
  balance += save
  print('Не хватает денег.')
print('Денег достаточно. Баланс =', balance)
