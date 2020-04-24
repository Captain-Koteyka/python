with open("my_file.txt", "w", encoding='UTF-8') as my_file:
    while True:
        user_data = input('Введите данные \n')
        my_file.write(user_data + '\n')
        if not user_data:
            break
my_file.close()
