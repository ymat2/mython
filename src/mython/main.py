import argparse
from importlib import metadata


__version__ = metadata.version("mython")


def main():
    parser = argparse.ArgumentParser(description="Personal python package.")
    parser.add_argument("-v", "--version", action="version", version=__version__, help="Show the version number")
    #subparsers = parser.add_subparsers(title="Commands", metavar="")
    args = parser.parse_args()
    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
