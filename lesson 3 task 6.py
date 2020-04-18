def int_func(a: str) -> str:
    return a.title()


my_string = map(int_func, input().split())
print(*my_string)
