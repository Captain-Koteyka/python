import json
with open('firms.txt', 'r', encoding='UTF-8') as firms:
    firms_dict = {}
    total_profit = 0
    number_of_firms = 0
    for line in firms:
        line = line.split()
        firm_profit = int(line[2]) - int(line[3])
        firms_dict[line[0]] = firm_profit
        if firm_profit >= 0:
            total_profit += firm_profit
            number_of_firms += 1
average_profit = total_profit / number_of_firms
average_profit_dict = {'average_profit': average_profit}
firm_list = [firms_dict, average_profit_dict]
print(firm_list)
with open('result.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(firm_list))
