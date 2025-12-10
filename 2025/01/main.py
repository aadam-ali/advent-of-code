import argparse


class Dial:
    def __init__(self, position: int):
        self.position = position
        self.stopped_at_zero_counter = 0
        self.zero_hit_counter = 0

    def turn(self, direction: str, clicks: int):
        modifier = -1 if direction == "L" else 1

        for _ in range(0, clicks):
            new_position = self.position + (1 * modifier)

            if new_position == -1 or new_position == 100:
                self.position = new_position % 100
            else:
                self.position = new_position

            if self.position == 0:
                self.zero_hit_counter += 1

           
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
        for ins in instructions:
            dial.turn(ins[0], ins[1])
        print(f"{dial.zero_hit_counter=}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
