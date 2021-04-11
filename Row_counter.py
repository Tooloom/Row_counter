import os
import argparse
from sys import platform

version = '1.2 (04.2021)'

# ---------------------------------- Selecting a special letter for the current OS -------------------------------------
if platform == "linux" or platform == "linux2":
    sp_letter = '/'
elif platform == "darwin" or platform == "win32":
    sp_letter = '\\'

# ------------------------------------------------ Preparing parser ----------------------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument('-e', type=str, help='File extension', default=False)
parser.add_argument('-d', '--direction', help='Searching direction', default=os.getcwd())
parser.add_argument('-n', help='Enable file counter', action='store_true')
parser.add_argument('-f', '--full', help='Enable summarize lines counts', action='store_true')
parser.add_argument('-v', help='Show program version', action='store_true')

args = parser.parse_args()


# -------------------------- Searching files with given extension to send them to row count function -------------------
def search(path, extension):
    count = [0, 0]
    try:
        for i in os.listdir(path):
            if os.path.isdir(path + sp_letter + i):
                temp = search(path + sp_letter + i, args.e)
                count = [x + y for x, y in zip(count, temp)]
            elif i.split('.')[-1] == extension:
                count[0] += 1
                count[1] += counter(path + sp_letter + i)
        return count
    except OSError:
        print('Wrong direction')
        return count


# -------------------------------------------------- Row count function ------------------------------------------------
def counter(path):
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for _ in file:
                count += 1
    except UnicodeDecodeError:
        print('File read error. Check if a file extension is valid')
        return count
    else:
        if args.n or args.full:
            return count
        else:
            print(f'Direction: {path}, lines:{count}')
            return count


# -------------------------------------------------------- Main --------------------------------------------------------
def main():
    if args.v:
        print(f'Row_counter version: [ {version} ]')
    elif args.e:
        if args.n:
            print(f'Founded files with extension [{args.e}]: {search(args.direction, args.e)[0]}')
        if args.full:
            print(f'Total lines in files with extension [{args.e}]: {search(args.direction, args.e)[1]}')
        else:
            search(args.direction, args.e)
    else:
        print('Error: the following arguments are required: -e\n[-h] for help')


if __name__ == "__main__":
    main()
