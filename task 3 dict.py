# через dict
seasons = {12: 'winter', 1: 'winter', 2: 'winter',
           3: 'spring', 4: 'spring', 5: 'spring',
           6: 'summer', 7: 'summer', 8: 'summer',
           9: 'autumn', 10: 'autumn', 11: 'autumn'}
month = input()
if month.isdigit():
    key = int(month)
    if 1 <= key <= 12:
        print(seasons[key])
