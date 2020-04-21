my_list = list(map(int, input().split()))
new_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index - 1]]
print(new_list)
