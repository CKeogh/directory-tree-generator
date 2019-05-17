#!/usr/bin/env python3

import argparse
from os import path, listdir
from colorama import Fore, init, deinit, Style

init(autoreset=True)

parser = argparse.ArgumentParser(
    description='display the directory tree for current working directory')
parser.add_argument('path', metavar='path/to/directory', type=str,
                    help='path to the directory to display tree of')

args = parser.parse_args()


def createTree(filePath, depth=0):
    if (not path.exists(filePath)):
        return 'Error: Invalid path'
    buff = '' if depth == 0 else '│      ' * (depth - 1) + '└──'

    # base case
    if (path.isfile(filePath)):
        return buff + path.basename(filePath) + '\n'

    # directory string
    treeString = buff + Fore.BLUE + Style.BRIGHT + \
        path.basename(filePath) + '\n' + Style.RESET_ALL

    for item in listdir(filePath):
        treeString += createTree(filePath + '/' + item, depth + 1)

    return treeString


thePath = args.path[0:-1] if args.path[-1] == '/' else args.path

print('\n\nAbsolute Path:' + Style.BRIGHT + Fore.GREEN + f'  {thePath}\n')
print(createTree(thePath))

deinit()
