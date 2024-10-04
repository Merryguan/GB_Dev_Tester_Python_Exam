import datetime


def print_notes(arr):
    for item in arr:
        print("Id: ", item['Id'],
              ", Дата создания: ", item['CreateDate'].strftime("%Y-%m-%d %H:%M:%S"),
              ", Дата модификации: ", item['ModifyDate'].strftime("%Y-%m-%d %H:%M:%S"),
              ", Заголовок: ", item['Title'],
              ", Текст: ", item['Note'], sep='')


def create_note(arr, id_add, title, note):
    create_date = datetime.datetime.today()
    arr.append({'Id': id_add, 'CreateDate': create_date, 'ModifyDate': create_date, 'Title': title, 'Note': note})


def search_id_note(arr, id_search):
    for i in range(len(arr)):
        if arr[i]['Id'] == id_search:
            return i
    return -1


def delete_note(arr, index_del):
    if index_del < len(arr):
        arr.pop(index_del)
        return 1
    return -1


def edit_note(arr, index_edit, menu_point):
    modify_date = datetime.datetime.now()
    if menu_point == 1:
        title_new = input("Введите новый заголовок заметки: ")
        arr[index_edit]['ModifyDate'] = modify_date
        arr[index_edit]['Title'] = title_new
    elif menu_point == 2:
        note_new = input("Введите новый текст заметки: ")
        arr[index_edit]['ModifyDate'] = modify_date
        arr[index_edit]['Note'] = note_new


def filter_by_date(arr, date_filter):
    list_filter = list()
    date1 = date_filter.strftime("%Y-%m-%d")
    print(date1)
    for item in arr:
        date2 = item['CreateDate'].strftime("%Y-%m-%d")
        if date1 == date2:
            list_filter.append(item)
    return list_filter


def write_csv(filename_out, arr):
    with (open(filename_out, 'w', encoding='utf-8') as notebook_out):
        for j in range(len(arr)):
            i = str(arr[j]['Id'])
            d1 = str(arr[j]['CreateDate'].strftime("%Y,%m,%d,%H,%M,%S"))
            d2 = str(arr[j]['ModifyDate'].strftime("%Y,%m,%d,%H,%M,%S"))
            t = arr[j]['Title']
            n = arr[j]['Note']
            s = '' + i + ";" + d1 + ";" + d2 + ";" + t + ";" + n
            notebook_out.write(f'{s}\n')


def read_csv(filename_in):
    new_notebook = list()
    list_of_fields = ['Id', 'CreateDate', 'ModifyDate', 'Title', 'Note']
    with open(filename_in, 'r', encoding='utf-8') as phone_book_in:
        for line in phone_book_in:
            list_of_raw = line[:-1].split(';')
            list_of_values = list()
            list_of_values.append(int(list_of_raw[0]))
            list_of_values.append(datetime.datetime.strptime(list_of_raw[1], "%Y,%m,%d,%H,%M,%S"))
            list_of_values.append(datetime.datetime.strptime(list_of_raw[2], "%Y,%m,%d,%H,%M,%S"))
            list_of_values.append(list_of_raw[3])
            list_of_values.append(list_of_raw[4])
            record = dict(tuple(zip(list_of_fields, list_of_values)))
            new_notebook.append(record)
    return new_notebook


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Вывести все заметки.\n"
          "2. Вывести заметки на дату.\n"
          "3. Добавить заметку.\n"
          "4. Удалить заметку.\n"
          "5. Показать заметку.\n"
          "6. Изменить заметку.\n"
          "7. Сохранить заметки в файл.\n"
          "8. Загрузить заметки из файла.\n"
          "9. Выход из программы\n")
    menu_point = int(input("Введите номер пункта меню: "))
    return menu_point


notebook = list()
idCount = 0

choice = show_menu()

while choice != 9:
    if choice == 1:
        print("Список всех заметок.")
        print_notes(notebook)
    elif choice == 2:
        print("Список заметок на дату.")
        date_input = input("Введите дату (ГГГГ-ММ-ДД): ")
        date_split = date_input.split("-")
        if len(date_split) < 3:
            print("Дата введена неверно.")
        elif int(date_split[1]) < 1 or 12 < int(date_split[1]):
            print("Неверно введен месяц.")
        elif int(date_split[2]) < 1 or 31 < int(date_split[2]):
            print("Неверно введен день")
        else:
            date = datetime.datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]))
            result_filter = filter_by_date(notebook, date)
            print_notes(result_filter)
    elif choice == 3:
        print("Добавление заметки.")
        head = input("Введите заголовок заметки: ")
        text = input("Введите текст заметки: ")
        create_note(notebook, idCount, head, text)
        index_find = search_id_note(notebook, idCount)
        list_print = list()
        list_print.append(notebook[index_find])
        print_notes(list_print)
        print("Заметка создана")
        idCount = idCount + 1
    elif choice == 4:
        print("Удаление заметки.")
        id_choice = int(input("Введите Id заметки: "))
        index_find = search_id_note(notebook, id_choice)
        if index_find == -1:
            print("Заметка не найдена")
        if index_find != -1:
            list_print = list()
            list_print.append(notebook[index_find])
            print_notes(list_print)
            result = delete_note(notebook, index_find)
            if result == 1:
                print("Заметка удалена")
            else:
                print("Заметка не удалена")
    elif choice == 5:
        print("Показать заметку.")
        id_choice = int(input("Введите Id заметки: "))
        index_find = search_id_note(notebook, id_choice)
        if index_find == -1:
            print("Заметка не найдена")
        if index_find != -1:
            list_print = list()
            list_print.append(notebook[index_find])
            print_notes(list_print)
    elif choice == 6:
        print("Редактирование заметки.")
        id_choice = int(input("Введите Id заметки: "))
        index_find = search_id_note(notebook, id_choice)
        if index_find == -1:
            print("Заметка не найдена")
        if index_find != -1:
            list_print = list()
            list_print.append(notebook[index_find])
            print_notes(list_print)
            print("\nВыберите необходимое действие:\n",
                  "1. Редактировать заголовок заметки.\n",
                  "2. Редактировать текст заметки.\n")
            menu_choice = int(input("Введите номер пункта меню: "))
            edit_note(notebook, index_find, menu_choice)
        list_print = list()
        list_print.append(notebook[index_find])
        print_notes(list_print)
        print("Заметка изменена.")
    elif choice == 7:
        print("Сохранение заметок в файл.")
        if len(notebook) == 0:
            print("Нет данных для сохранения.")
        else:
            write_csv("notebook.csv", notebook)
            print("Заметки сохранены.")
    elif choice == 8:
        print("Загрузка заметок из файла.")
        notebook = read_csv("notebook.csv")
        idCount = len(notebook) + 1
        print("Заметки загружены.")

    choice = show_menu()
