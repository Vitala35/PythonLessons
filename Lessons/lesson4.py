# Є список певних країн, перевіряти чи країна яку вводить користувач є в цьому спису.
# Якщо є то вивести текст: <nameCounty> добрий ранок!
# Якщо ні, вивести <nameCountry> - не знайдено!


# country = ['Italy', 'French', 'Ukraine', 'Spain', 'Denmark']
# write_text = input('Your text: ')
#
# if write_text in country:
#     print(f'Good morning, {write_text}')
# else:
#     print(f'Dont found, {write_text}')



# 2) Користувач вводить назву країни, програма виводить: привіт, <назва країни>, розробити для 5-тьох країн.
# Якщо країна не описана умовною конструкцією то виводити: не відома країна.


# country = input('Write country: ')
# if country == 'Ukraine':
#     print(f'Hallo, {country}')
# elif country == 'Spain':
#     print(f'Hallo, {country}')
# elif country == 'French':
#     print(f'Hallo, {country}')
# elif country == 'Denmark':
#     print(f'Hallo, {country}')
# elif country == 'Italy':
#     print(f'Hallo, {country}')
# else:
#     print(f'lost, {country}')



# Написати програму яка приймає країну та час (daytime).
# Якщо находить певну країну то дивиться який в ній daytime і залежно від цього повертає good morning, <country> or good evening <country>.

country = input('Enter country name: ')

if country == 'Ukraine':
    day_time = input('Enter day time: ')
    if day_time == 'morning':
        print(f'good morning {country}')
    elif day_time == 'evening':
        print(f'good evening {country}')


elif country == 'French':
    day_time = input('Enter day time: ')
    if day_time == 'morning':
        print(f'good morning {country}')
    elif day_time == 'evening':
        print(f'good evening {country}')


elif country == 'Denmark':
    day_time = input('Enter day time: ')
    if day_time == 'morning':
        print(f'good morning {country}')
    elif day_time == 'evening':
        print(f'good evening {country}')


elif country == 'Italy':
    day_time = input('Enter day time: ')
    if day_time == 'morning':
        print(f'good morning {country}')
    elif day_time == 'evening':
        print(f'good evening {country}')


elif country == 'Spain':
    day_time = input('Enter day time: ')
    if day_time == 'morning':
        print(f'good morning {country}')
    elif day_time == 'evening':
        print(f'good evening {country}')