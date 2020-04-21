my_list = list(map(int, input().split()))
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
