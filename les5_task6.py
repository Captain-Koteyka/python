subjects = open('subjects.txt', 'r', encoding='UTF-8')
subjects_dict = {}
for line in subjects:
    line = line.split()
    subject = line[0][:-1]
    hours = 0
    for itm in line[1:]:
        itm = ''.join(x for x in itm if x.isdigit())
        if itm != '':
            hours += int(itm)
    subjects_dict[subject] = hours
subjects.close()
print(subjects_dict)
