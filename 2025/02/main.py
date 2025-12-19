import argparse
from typing import Callable


def is_invalid_id(id_: int):
    stringified_id = str(id_)
    string_length = len(stringified_id)

    if string_length % 2 == 0:
        half_length = string_length // 2
        return stringified_id[:half_length] == stringified_id[half_length:]

    return False


def is_invalid_id_2(id_: int):
    stringified_id = str(id_)
    string_length = len(stringified_id)

    factors = []
    for i in range(1, int(string_length**0.5) + 1):
        if string_length % i == 0:
            factors.extend([i, int(string_length / i)])

    for factor in factors:
        if factor != string_length:
            if stringified_id[:factor] * int(string_length / factor) == stringified_id:
                return True

    return False


def find_invalid_ids(min: int, max: int, func: Callable[[int], bool]) -> list[int]:
    invalid_ids = []

    for id_ in range(min, max + 1):
        if func(id_):
            invalid_ids.append(id_)

    return invalid_ids


def main(argv: list[str] | None = None) -> int:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("challenge", type=int, choices=[1, 2])
    argparser.add_argument("filename")
    args = argparser.parse_args(argv)

    with open(args.filename, "r") as f:
        input_data = f.read().splitlines()[0].split(",")

    if args.challenge == 1:
        invalid_ids = []

        for id_range in input_data:
            min, max = id_range.split("-")
            invalid_ids.extend(find_invalid_ids(int(min), int(max), is_invalid_id))

        sum_of_invalid_ids = sum(invalid_ids)
        print(f"{sum_of_invalid_ids=}")
    elif args.challenge == 2:
        invalid_ids = []

        for id_range in input_data:
            min, max = id_range.split("-")
            invalid_ids.extend(find_invalid_ids(int(min), int(max), is_invalid_id_2))

        sum_of_invalid_ids = sum(invalid_ids)
        print(f"{sum_of_invalid_ids=}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
