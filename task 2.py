newList = input().split(' ')
index = 0
if len(newList) % 2 == 1:
    while index < len(newList) - 1:
        newList[index], newList[index + 1] = newList[index + 1], newList[index]
        index += 2
    print(newList)
if len(newList) % 2 == 0:
    while index < len(newList):
        newList[index], newList[index + 1] = newList[index + 1], newList[index]
        index += 2
    print(newList)
