import math

#
# a = float(input('Enter number a:'))
# b = float(input('Enter number b:'))
# c = float(input('Enter number c:'))
#
# p = (a + b + c) / 2
#
# print(math.sqrt(p * (p - a) * (p - b) * (p - c)))

# question = input('Please enter any figure:')
# if question == 'Triange':
#     a = float(input('Enter number a:'))
#     b = float(input('Enter number b:'))
#     c = float(input('Enter number c:'))
#     p = (a + b + c) / 2
#     print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
# elif question == 'Rectangle':
#     a = float(input('Enter number a:'))
#     b = float(input('Enter number b:'))
#     print(a * b)
# elif question == 'Circle':
#     r = float(input('Enter number r:'))
#     print(3.14 * (r ** 2))

# a = int(input('Enter number a:'))
# if a > -15 and a <= 12 or a > 14 and a < 17 or a > 19:
#     print(True)
# else:
#     print(False)

a = float(input('Enter number a:'))
b = float(input('Enter number b:'))
option = input('Enter option')
if option == '+':
    print(a + b)
if option == '-':
    print(a - b)
if option == '/':
    print(a / b)
if option == '*':
    print(a * b)

