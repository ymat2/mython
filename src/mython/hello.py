import os

def main():
    user = os.environ.get("USER")
    msg = "Hello, " + user
    print(msg)


if __name__ == "__main__":
    main()
