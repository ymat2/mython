import argparse
import re
import sys
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern")
    parser.add_argument("infile", nargs="*")
    args = parser.parse_args()
    return args


def grep_pattern_from_file(pttrn: str, file: Path) -> list:
    grep_result = []
    with open(file) as f:
        for line in f:
            if re.search(pttrn, line):
                line = re.sub(pttrn, r"\033[31m\g<0>\033[0m", line)
                grep_result.append(line.rstrip("\n"))
    return grep_result


def grep_pattern_from_stdin(pttrn: str, lines):
    grep_result = []
    for line in lines:
        if re.search(pttrn, line):
            line = re.sub(pttrn, r"\033[31m\g<0>\033[0m", line)
            grep_result.append(line)
    return grep_result


def main():
    args = parse_arguments()

    if len(args.infile) > 0:
        for f in args.infile:
            for line in grep_pattern_from_file(args.pattern, f):
                print(line)
    else:
        line = sys.stdin.read()
        for line in grep_pattern_from_stdin(args.pattern, line.split("\n")):
            print(line)


if __name__ == "__main__":
    main()
