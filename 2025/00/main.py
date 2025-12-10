import argparse


def main(argv: list[str] | None = None) -> int:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("challenge", type=int, choices=[1, 2])
    argparser.add_argument("filename")
    args = argparser.parse_args(argv)

    with open(args.filename, "r") as f:
        input_data = f.read().splitlines()

    if args.challenge == 1:
        print("challenge 1...")
    elif args.challenge == 2:
        print("challenge 2...")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
