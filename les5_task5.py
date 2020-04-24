from functools import reduce
my_file = open('my_file.txt', 'w')
my_file.write('1 3 39 80 14 1234 342')
my_file.close()
new_file = open('my_file.txt', 'r')
num_list = []
for line in new_file:
    line = line.split()
    for itm in line:
        itm = int(itm)
        num_list.append(itm)
sum_of_num = reduce(lambda a, b: a + b, num_list)
new_file.close()
print(sum_of_num)
