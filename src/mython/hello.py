import os


def main():
    users = ["USER", "USERNAME", "user"]
    user = next((os.environ.get(k) for k in users if k in os.environ), "anonymous")
    print("Hello, " + user)


if __name__ == "__main__":
    main()
