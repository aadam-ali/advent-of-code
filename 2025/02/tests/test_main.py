import pytest
from main import find_invalid_ids
from main import is_invalid_id
from main import is_invalid_id_2
from main import main


class TestChallenge1:
    @pytest.mark.parametrize("id", (55, 6464, 123123))
    def test_is_invalid_id_when_invalid_id(self, id):
        result = is_invalid_id(id)

        assert result == True

    @pytest.mark.parametrize("id", (54, 6463, 123122, 1, 234, 1234123, 121212))
    def test_is_invalid_id_when_valid_id(self, id):
        result = is_invalid_id(id)

        assert result == False

    @pytest.mark.parametrize(
        "min,max,expected",
        [
            (11, 22, [11, 22]),
            (95, 115, [99]),
            (998, 1012, [1010]),
            (1188511880, 1188511890, [1188511885]),
            (222220, 222224, [222222]),
            (1698522, 1698528, []),
        ],
    )
    def test_find_invalid_ids(self, min, max, expected):
        result = find_invalid_ids(min, max, is_invalid_id)

        assert result == expected

    def test_main(self, capsys):
        main(["1", "tests/test_input.txt"])

        output = capsys.readouterr()

        assert output.out == "sum_of_invalid_ids=1227775554\n"


class TestChallenge2:
    @pytest.mark.parametrize("id", (55, 6464, 123123, 2121212121))
    def test_is_invalid_id_when_invalid_id(self, id):
        result = is_invalid_id_2(id)

        assert result == True

    @pytest.mark.parametrize("id", (54, 6463, 123122, 1, 234, 1234123))
    def test_is_invalid_id_when_valid_id(self, id):
        result = is_invalid_id_2(id)

        assert result == False

    @pytest.mark.parametrize(
        "min,max,expected",
        [
            (11, 22, [11, 22]),
            (95, 115, [99, 111]),
            (998, 1012, [999, 1010]),
            (1188511880, 1188511890, [1188511885]),
            (222220, 222224, [222222]),
            (1698522, 1698528, []),
        ],
    )
    def test_find_invalid_ids(self, min, max, expected):
        result = find_invalid_ids(min, max, is_invalid_id_2)

        assert result == expected

    def test_main(self, capsys):
        main(["2", "tests/test_input.txt"])

        output = capsys.readouterr()

        assert output.out == "sum_of_invalid_ids=4174379265\n"
