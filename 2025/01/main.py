import argparse


class Dial:
    def __init__(self, position: int):
        self.position = position
        self.stopped_at_zero_counter = 0

    def turn(self, direction: str, clicks: int):
        if direction == "L":
            clicks = -clicks

        self.position = (self.position + clicks) % 100

        if self.position == 0:
            self.stopped_at_zero_counter += 1


def main(argv: list[str] | None = None) -> int:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("challenge", type=int, choices=[1, 2])
    argparser.add_argument("filename")
    args = argparser.parse_args(argv)

    dial = Dial(50)
    with open(args.filename, "r") as f:
        input_data = f.read().splitlines()

    instructions = [(ins[:1], int(ins[1:])) for ins in input_data]

    if args.challenge == 1:
        for ins in instructions:
            dial.turn(ins[0], ins[1])
        print(f"{dial.stopped_at_zero_counter=}")
    elif args.challenge == 2:
        print("challenge 2...")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
