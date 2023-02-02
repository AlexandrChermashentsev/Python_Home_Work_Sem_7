import data_provider as dp
import view

def Buttom():
    user_choice = view.Enter_Choice() # Главное меню. Выбор между созданием нового файла и напечатанием внешнего файла в терминале
    if user_choice == '1': # Выбор в пользу нового файла
        path = view.File_Name() # Пишем имя нового файла
        user_choice = view.Choice_Metod() # Даем выбрать между написанием файла в строку или в столбец
        if user_choice == '1': # В строку
            dp.Create_CSV_Line(path) # Создаем Шапку файла
            while user_choice.lower() != 'q':
                user_choice = view.Action_Choice() # Пока пользователь не нажмет команду "q" он может добавлять новые контакты или эскпортировать из внешнего файла
                if user_choice == '1':
                    dp.Import_Data_Line(dp.Create_New_Contact(), path) # Создание нового контакта
                elif user_choice == '2': # Пользователь выбирает экспортировать данные из фнешнего файла 
                    path = view.Enter_Path() # Прописываем путь к файлу из которого будем брать данные
                    for i in dp.Export_Data_Line(path): # Экспортируем
                        dp.Import_Data_Line(i) # Импортируем в строку.

        elif user_choice == '2': # В столбец
            dp.Create_CSV_Row(path) # Создаем новый файл в столбец
            while user_choice.lower() != 'q':
                user_choice = view.Action_Choice() # Выбираем между созданием нового контакта и экспортом из внешнего файла
                if user_choice == '1':
                    dp.Import_Data_Row(dp.Create_New_Contact(), path) # Создаем новый контакт в столбец
                elif user_choice == '2':
                    user_choice = view.Choice_My_Data_Or_Any() # Выбор между стандартной формой записи данных(как в условии задачи) и созданной этой программой
                    if user_choice == '1':
                        path_exp = view.Enter_Path() # Вбиваем путь к внешнему файлу
                        dp.Imp_Exp_Data_Row_My_Data(dp.Export_Data_Row_My_Data(path_exp), path) # Вносим в нашу базу данных, конвертируя в нужный мне формат
                    elif user_choice == '2':
                        path_exp = view.Enter_Path() # Вбиваем путь к внешнему файлу
                        dp.Import_Data_Row(dp.Export_Data_Row_Any(path_exp), path) #  # Вносим в нашу базу данных, конвертируя в нужный мне формат
    elif user_choice == '2': 
        path = view.Enter_Path() # Пишем путь к внешнему файлу
        dp.Export_And_Print_Data_In_Terminal(path) # Печатаем данные файла в терминале