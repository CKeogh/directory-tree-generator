import argparse
from os import path, listdir

parser = argparse.ArgumentParser(
    description='display the directory tree for current working directory')
parser.add_argument('path', metavar='path/to/directory', type=str,
                    help='path to the directory to display tree of')

args = parser.parse_args()


def createTree(filePath):
    if (not path.exists(filePath)):
        return 'Error: Invalid path'

    if (path.isfile(filePath)):
        return '-' + path.basename(filePath)

    treeString = path.basename(filePath) + '\n'
    for item in listdir(filePath):

        treeString += '|' + createTree(filePath + '/' + item) + '\n'

    return treeString


print(createTree(args.path))
