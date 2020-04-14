new_string = input()
my_list = new_string.split(' ')
number_of_string = 1
for itm in my_list:
    if len(itm) <= 10:
        print(number_of_string, itm)
        number_of_string += 1
    else:
        print(number_of_string, itm[:10])
        number_of_string += 1
