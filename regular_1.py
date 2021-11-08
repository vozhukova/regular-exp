from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding="UTF-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# Задача 1
for contact in contacts_list[1:]:
    name = contact[0]+" "+contact[1]+" "+contact[2]
    spaces = re.sub("  ", "", name)
    spaces_splitted = re.split(" ", spaces)
    contact[0:3] = spaces_splitted[0:3]

# Задача 2
for contact in contacts_list[1:]:
    tel = contact[-2]
    pattern1 = r"(\+7|8)?[\s\(-]*(\d{3})[\)\-\s]*(\d{3})\-*(\d{2})\-*(\d+)"
    subst1 = r"+7(\2)\3-\4-\5"
    tel_number = re.sub(pattern1, subst1, tel)
    pattern2 = r"\(*([а-я]{0,3}\.)\s(\d{0,4})\)*"
    subst2 = r"\1\2"
    tel_number2 = re.sub(pattern2, subst2, tel_number)
    contact[-2] = tel_number2

# Задача 3
dict = {}
# Добавляем данные в словарь, где ключ фамилия+имя
for contact in contacts_list:
    name_dict = str(contact[0:2])
    if name_dict in dict.keys():
        for i in contact[2:7]:
            dict[name_dict].append(i)
    else:
        dict[name_dict] = contact[2:7]
    # Удаляем дубли в values
    for key in dict.keys():
        list1 = dict[key]
        list2 = []
        [list2.append(x) for x in list1 if x not in list2]
        dict[key] = list2

# Структурируем values
dict["['Мартиняхин', 'Виталий']"][2] = dict["['Мартиняхин', 'Виталий']"][4]
del dict["['Мартиняхин', 'Виталий']"][4]
for key, item in dict.items():
    if len(item) < 5:
        dict[key].append("")

# Добавляем полученный результат в список
result = []
for key, item in dict.items():
    k1 = key.strip("[")
    k2 = k1.strip("]")
    k3 = k2.replace("'", "")
    mix = k3.split(", ") + item
    result.append(mix)

with open("phonebook.csv", "w", encoding="UTF-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result)

