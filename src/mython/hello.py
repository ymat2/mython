import os

def main():
    user = os.environ.get("USER")
    print("Hello, " + user)


if __name__ == "__main__":
    main()
