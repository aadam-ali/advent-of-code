import pytest
from main import main


class TestChallenge1:
    def test_main(self, capsys):
        main(["1", "tests/test_input.txt"])

        output = capsys.readouterr()

        assert output.out == "challenge 1...\n"


class TestChallenge2:
    def test_main(self, capsys):
        main(["2", "tests/test_input.txt"])

        output = capsys.readouterr()

        assert output.out == "challenge 2...\n"
