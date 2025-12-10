import pytest
from main import Dial
from main import main


class TestChallenge1:
    @pytest.mark.parametrize(
        "direction,clicks,expected",
        [
            ("L", 200, 50),
            ("L", 30, 20),
            ("L", 51, 99),
            ("R", 200, 50),
            ("R", 30, 80),
            ("R", 50, 0),
        ],
    )
    def test_turn(self, direction, clicks, expected):
        dial = Dial(50)

        dial.turn(direction, clicks)

        assert dial.position == expected

    @pytest.mark.parametrize(
        "direction,clicks,expected",
        [
            ("L", 200, 0),
            ("L", 30, 0),
            ("L", 50, 1),
            ("R", 200, 0),
            ("R", 30, 0),
            ("R", 50, 1),
        ],
    )
    def test_stopped_on_zero(self, direction, clicks, expected):
        dial = Dial(50)

        dial.turn(direction, clicks)

        assert dial.stopped_at_zero_counter == expected

    def test_main(self, capsys):
        main(["1", "tests/test_input.txt"])

        output = capsys.readouterr()

        assert output.out == "dial.stopped_at_zero_counter=3\n"


class TestChallenge2:
    @pytest.mark.parametrize(
        "direction,clicks,expected",
        [
            ("L", 200, 2),
            ("L", 30, 0),
            ("L", 50, 1),
            ("L", 55, 1),
            ("R", 200, 2),
            ("R", 30, 0),
            ("R", 50, 1),
            ("R", 55, 1),
        ],
    )
    def test_stopped_on_zero(self, direction, clicks, expected):
        dial = Dial(50)

        dial.turn(direction, clicks)

        assert dial.zero_hit_counter == expected

    @pytest.mark.parametrize(
        "direction,clicks",
        [
            ("L", 5),
            ("R", 5),
        ],
    )
    def test_stopped_on_zero_starts_at_0(self, direction, clicks):
        dial = Dial(0)

        dial.turn(direction, clicks)

        assert dial.zero_hit_counter == 0

    def test_main(self, capsys):
        main(["2", "tests/test_input.txt"])

        output = capsys.readouterr()

        assert output.out == "dial.zero_hit_counter=6\n"
