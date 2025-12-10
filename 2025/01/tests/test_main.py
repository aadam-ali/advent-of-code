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
