def user_data_func(**kwargs):
    name = input('Введите имя\n')
    surname = input('Введите фамилию\n')
    birth_year = input('Введите год рождения\n')
    city = input('Введите город проживания\n')
    email = input('Введите email\n')
    phone_number = input('Введите номер телефона\n')
    user_data_dict = {'name': name,
                      'surname': surname,
                      'birth year': birth_year,
                      'city': city,
                      'email': email,
                      'phone number': phone_number}
    return user_data_dict


n = user_data_func()
print(n)
