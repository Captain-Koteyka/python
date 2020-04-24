with open("new_file.txt", "r", encoding='UTF-8') as my_file:
    number_of_lines = 0
    number_of_words = 0
    for line in my_file:
        number_of_lines += 1
        for word in line.split(' '):
            number_of_words += 1
        print('Количество слов в строке ', number_of_lines, ': ', number_of_words, sep='')
        number_of_words = 0
print('Количество строк:', number_of_lines)
my_file.close()