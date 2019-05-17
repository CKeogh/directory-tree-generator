# directory-tree-generator

A simple CLI for displaying a directory tree. Give a path as the argument to show tree of all files and directories from that path.

## Getting Started

Clone this repo to your local machine and create a Python virtual environment using **venv** or **env**.

## dependencies

You will need the following dependencies installed on your local machine:
* argparse
* colorama

## Using The CLI

simply call the the treeGenerator.py script in the command line with the directory path as its argument:

```
python3 treeGenerator.py /path/to/directory
```

## Output

The command line output should look like the example:

```console
Absolute Path:  /absolute/path/to/tree-test

tree-test
└──2ndLayerDir1
│      └──3rdLayerFile1.txt
└──2ndLayerDir2
│      └──3rdLayerFile1.txt
│      └──3rdLayerDir1
│      │      └──4thLayerFile1.txt
│      └──3rdLayerFile2.txt
└──2ndLayerFile2.txt
└──2ndLayerFile1.txt
```