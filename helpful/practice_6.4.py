# Andrey Malakanov
# Skillbox PythonBasic

# Practice 6.4 - 1 
print('Задача 1. Неправильный таймер')

# Петя писал таймер для телефона, но у него что-то пошло не так.

#count = 0
#While count <= 10
# if count == 0:
#   print('Время вышло!')
# else:
#   print(count)
#   count -= 1

# Скопируйте программу в редактор, исправьте ошибки и убедитесь, что на экран выводятся числа с 10 до 0 и сообщение «Время вышло!».

print()
count = 10
while count >= -1:
  if count < 0:
    print('Время вышло!')
    break
  else:
    print(count)
    count -= 1
print()
print('========================================')
print()


# Practice 6.4 - 2 
print('Задача 2. Тестируем приложение')
print()
# Напишите программу, которая имитирует работу с приложением: программа спрашивает у пользователя «Продолжаем работать? 1/0: » до тех пор, пока пользователь не введёт 0, — после этого выводится сообщение: «Приложение закрывается…». В конце программы также выводится сообщение: «Работа завершена». Для создания бесконечного цикла используйте while True.

cont_work = 1
while cont_work:
  cont_work = int(input('Продолжаем работать? 1/0: '))
print('Приложение закрывается…')
print('Работа завершена')
print()
print('========================================')
print()


# Practice 6.4 - 3
print('Задача 3. Вирус')
print()
# Дима написал программу-вирус специально для того, чтобы проучить своего друга-должника, который никак не хочет возвращать скейтборд. Программа не даёт работать за компьютером и постоянно выводит на экран сообщение «Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!». Как только вводится правильный код, вирус удаляется. Напишите такую же программу, которую написал Дима.

#Пример:
#Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
#Введите код: 1005
#Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
#Введите код: 7777
#Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
#Введите код: 0550
#Код верный, завершаю работу...

# while True:
while 1 > 0: # Если выбрать условие while True: при вводе 0 цикл воспринимает его как False и его работа завершается.
  code = input('Введите код: ')
  if code != '0550':
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
  else:
    print('Код верный, завершаю работу...')
    break