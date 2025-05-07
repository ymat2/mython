import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="User name.")
    args = parser.parse_args()
    if args.user:
        user = args.user
    else:
        users = ["USER", "USERNAME", "user"]
        user = next((os.environ.get(k) for k in users if k in os.environ), "anonymous")
    print("Hello, " + user)


if __name__ == "__main__":
    main()
