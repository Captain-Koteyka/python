my_list = [7, 5, 3, 3, 2]
new_number = input()
if new_number.isdigit():
    new_number = int(new_number)
if new_number > my_list[0]:
    my_list.insert(0, new_number)
elif new_number <= my_list[-1]:
    my_list.append(new_number)
else:
    index = 0
    while my_list[index] >= new_number:
        index += 1
    my_list.insert(index, new_number)
print(my_list)
