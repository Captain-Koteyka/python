seasons = ['winter', 'winter',
           'spring', 'spring', 'spring',
           'summer', 'summer', 'summer',
           'autumn', 'autumn', 'autumn',
           'winter']
month = input()
if month.isdigit():
    index = int(month)
    if 1 <= index <= 12:
        print(seasons[index - 1])
