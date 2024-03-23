from return_data_file import data_file

def copy_data():
    data, nf = data_file()

    answer = int(input("Выберите файл, в который планируете перенести данные: "))
    while(answer < 1 or answer > 2) or answer == nf:
        answer = int(input("Ошибка! Вы ввели некорректное значение или выбрали тот же файл\n",
                        "Выберите файл, в который планируете перенести данные: "))
    
    with open(f'db\data_{answer}.txt', 'r', encoding='utf-8') as file:
        count_row_end_data = len(file.readlines()) + 1
        
    data = [f'{i + count_row_end_data};{data[i].split(";")[1]};'
            f'{data[i].split(";")[2]};'
            f'{data[i].split(";")[3]};'
            f'{data[i].split(";")[4]}'
            for i in range(len(data))]
    
    with open(f'db\data_{answer}.txt', 'a', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно скопированны")
    