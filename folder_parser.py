# -*- coding: utf-8 -*-
"""
Console Tree parse.
For parse in folders and sub-folders all files recursively and put it in output folder
"""


import argparse
from pathlib import Path
import shutil


def parse_argv():
    """ Method for parsing arguments for this script
    """
    parser = argparse.ArgumentParser(description="Copy all files from tree of folder in another folder")
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Source path with folders/files"
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=Path('dist'), help="Output folder"
    )
    return parser.parse_args()


def recursive_copy(source: Path, output: Path):
    """ Method for recursive parsing of folders and sub-folders
    :param source: Path to source folder
    :param output:  Path to output folder
    :type source: Path
    :type output: Path
    """
    for el in source.iterdir():
        if el.is_dir():
            recursive_copy(el, output)
        else:
            split_name = el.name.split('.')
            if len(split_name) < 2:
                folder = 'others'
            else:
                folder = split_name[-1]
            folder = Path(output, folder)
            folder.mkdir(exist_ok=True, parents=True)
            shutil.copy(el, folder)


def main():
    args = parse_argv()
    recursive_copy(args.source, args.output)


if __name__ == "__main__":
    main()
