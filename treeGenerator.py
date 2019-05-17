import argparse

parser = argparse.ArgumentParser(description='display the directory tree for current working directory')
parser.add_argument('path', metavar='path/to/directory', type=str,
                    help='path to the directory to display tree of')
