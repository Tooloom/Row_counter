import os
import argparse

version = '1.0 (04.2021)'


# ----------------------------------------- Подготовка парсера аргументов ----------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument('-e', type=str, help='File extension', default=False)
parser.add_argument('-d', '--dir', help='Searching direction', default=os.getcwd())
parser.add_argument('-n', help='Enable file counter', action='store_true')
parser.add_argument('-v', help='Show program version', action='store_true')

args = parser.parse_args()


# --------- Поиск файлов с указанным расширением с последующей передайчей их в функцию для поиска кол-ва строк ---------
def search(path, extension):
    count = 0
    try:
        for i in os.listdir(path):
            if os.path.isdir(path + '\\' + i):
                count += search(path + '\\' + i, args.e)
            elif i.split('.')[-1] == extension:
                count += 1
                counter(path + '\\' + i)
        return count
    except OSError:
        print('Ошибка в указании пути.')
        return 0


# -------------------------------------------- Функция по поиску кол-ва строк ------------------------------------------
def counter(path):
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for _ in file:
                count += 1
    except UnicodeDecodeError:
        print('Ошибка при чтении. Проверьте корректность введённых данных.')
    else:
        print(f'Direction: {path}, lines:{count}')


# -------------------------------------------------------- Main --------------------------------------------------------
def main():
    if args.v:
        print(f'Row_counter version: {version}')
    elif args.e:
        if args.n:
            print(f'Найденных файлов с расширением {args.e}: ', search(args.dict, args.e))
        else:
            search(args.dir, args.e)
    else:
        print('Error: the following arguments are required: -e\n[-h] for help')


if __name__ == "__main__":
    main()
