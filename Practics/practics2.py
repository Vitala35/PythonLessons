# Написати простий каркулятор для двох чесел (a i b).
# З наступними математичними операціями: +, -, *, /, pow. Числа а і b - приймаються від користувача.
# Відповідь при діленні і множенні має заокруглюватися до двох чисел після коми.
# a = float(input('first number:'))
# b = float(input('second number:'))
# operation = input('enter operation: ')
#
# if operation == '+':
#     print(a + b)
# elif operation == '-':
#     print(a - b)
# elif operation == '*':
#     print(a * b)
# elif operation == '/':
#     print(a / b)
# elif operation == 'pow':
#     print(a ** b)

a = float(input('Enter min time'))
b = float(input('Enter max time'))
h = float(input('Enter present time'))

if h > b:
    print('up')
elif h < a:
    print('down')
elif h > a and h < b:
    print('normal')


