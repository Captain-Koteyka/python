with open('salary.txt', 'r', encoding='UTF-8') as my_file:
    number_of_employees = 0
    salary = 0
    for line in my_file:
        number_of_employees += 1
        line = line.split(' ')
        salary += int(line[1])
        if int(line[1]) < 20000:
            print(line[0])
    average_salary = salary / number_of_employees
    print("{:.2f}".format(average_salary))
my_file.close()
