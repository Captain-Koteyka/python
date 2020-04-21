from itertools import (count,
                       cycle,
                       )
from time import sleep
# Бесконечный итератор, генерирующий целые числа, начиная с указанного
reference_point = int(input())
for el in count(reference_point):
    print(el)
    sleep(1)


# Бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее
my_list = input().split()
for el in cycle(my_list):
    print(el)
    sleep(0.5)
