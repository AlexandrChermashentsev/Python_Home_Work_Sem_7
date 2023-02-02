import csv
import os
import view


os.system('clear')
FILENAME = 'Telephone_book.csv'

def Create_New_Contact():
    global surname
    global name
    global telephone
    global comment
    global data
    surname = view.Get_Surname()
    name = view.Get_Name()
    telephone = view.Get_Telephone_Number()
    comment = view.Get_Comment()
    data = [surname, name, telephone, comment]
    return data

def Create_CSV_Line(FILENAME):
    title = ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    with open(FILENAME, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(title)

def Create_CSV_Row(FILENAME):
    title = ['Справочник в столбик']
    with open(FILENAME, 'w', newline="") as file:
        for i in title:
            writer = csv.writer(file)
            writer.writerow(i.split('-'))

def Import_Data_Line(list_my, FILENAME):
    with open(FILENAME, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(list_my)

def Import_Data_Row(new_contact, path):
    title = ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    tuple_1 = []
    for i in range(len(title)):
        tuple_1.append((title[i].split() + new_contact[i].split()))
    with open (path, 'a', newline='') as file:
        for i in tuple_1:
            writer = csv.writer(file)
            writer.writerow(i)
        writer.writerow('')

def Export_Data_Line(path):
    exp_data = []
    with open(path, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if not 'Фамилия' in row:
                exp_data.append(row)
    return exp_data

def Imp_Exp_Data_Row_My_Data(new_contact, path):
    with open (path, 'a', newline='') as file:
        for i in new_contact:
            writer = csv.writer(file)
            writer.writerow(i)
        writer.writerow('')

def Export_Data_Row_My_Data(path):
    exp_data = []
    with open(path, newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            if 'Фамилия' in line or 'Имя' in line or\
                'Телефон' in line or 'Комментарий' in line:
                exp_data.append(line)
    return exp_data

def Export_Data_Row_Any(path):
    exp_data = []
    with open(path, newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            exp_data.append(line)
    return exp_data

def Export_And_Print_Data_In_Terminal(path):
    with open(path, newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)