my_file = open('my_file.txt', 'r', encoding='UTF-8')
new_file = open('new_file.txt', 'w', encoding='UTF-8')
num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for line in my_file:
    line = line.split()
    line[0] = num_dict.get(line[0])
    new_line = ' '.join(line)
    new_file.write(new_line + '\n')
my_file.close()
new_file.close()
