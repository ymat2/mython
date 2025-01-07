import argparse
import os

from importlib import metadata


__version__ = metadata.version("mython")


def parse_args():
    parser = argparse.ArgumentParser(description="Personal python package.")
    parser.add_argument("-v", "--version", action="version", version=__version__, help="Show the version number")
    parser.add_argument("-u", "--user", help="User name.")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.user:
        user = args.user
    else:
        users = ["USER", "USERNAME", "user"]
        user = next((os.environ.get(k) for k in users if k in os.environ), "anonymous")
    print("Hello, " + user)


if __name__ == "__main__":
    main()
