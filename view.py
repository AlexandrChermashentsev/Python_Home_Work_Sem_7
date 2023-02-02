def Get_Surname():
    return input('Введите фамилию: ')

def Get_Name():
    return input('Введите имя: ')

def Get_Telephone_Number():
    return input('Введите номер телефона: ')

def Get_Comment():
    return input('Кем для вас является этот человек: ')

def Action_Choice():
    return input(
'Что хотите сделать?\n\
"1" - Создать новый контакт.\n\
"2" - Экспортировать из другой базы.\n\
Выйти -> "q"\n-> '
)

def Enter_Choice():
    return input('"1" - Создать новый\n\
"2" - Открыть документ в терминале\n-> ')

def Choice_Metod():
    return input('В каком формате будем записывать контакты?\n\
"1" - В строку\n\
"2" - В столбец\n\
-> ')

def Enter_Path():
    return input('Введите полный путь к файлу\n-> ') + '.csv'

def File_Name():
    f_name = input('Введите имя нового файла: ') + '.csv'
    return f_name

def Choice_My_Data_Or_Any():
    return input('Вы хотите импортировать из базы данных \
созданной этой программой или в формате по условию задачи?\n\
"1" - В этой программе\n\
"2" - Как в README.txt\n-> ')