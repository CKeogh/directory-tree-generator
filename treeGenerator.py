import argparse
from os import path, listdir

parser = argparse.ArgumentParser(
    description='display the directory tree for current working directory')
parser.add_argument('path', metavar='path/to/directory', type=str,
                    help='path to the directory to display tree of')

args = parser.parse_args()


def createTree(filePath, depth):
    if (not path.exists(filePath)):
        return 'Error: Invalid path'

    lines = '└──' if depth == 0 else '│      ' * (depth - 1) + '└──'

    # base case
    if (path.isfile(filePath)):
        return lines + path.basename(filePath) + '\n'

    # directory string
    treeString = lines + path.basename(filePath) + '\n'

    for item in listdir(filePath):
        treeString += createTree(filePath + '/' + item, depth + 1)

    return treeString


print(createTree(args.path, 0))
