import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", type=int)
    args = parser.parse_args()
    print(fizzbuzz(args.number))


def fizzbuzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        msg = "fizzbuzz"
    elif num % 3 == 0:
        msg = "fizz"
    elif num % 5 == 0:
        msg = "buzz"
    else:
        msg = str(num)
    return msg


if __name__ == "__main__":
    main()
