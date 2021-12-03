from unittest import mock

import pytest

from homework04.task_2_mock_input import count_dots_on_i

test_data = [
    (["iii asd eqw\nasd iii", 200], 6),
    (["no I\nabsolutely no", 200], 0),
    (["iii", 400], "error"),
]


@pytest.mark.parametrize("test_input, expected", test_data)
def test_count_i(test_input, expected):
    def fake_get(url, *args, **kwargs):
        class FakeResponse:
            text, status_code = test_input

        return FakeResponse()

    with mock.patch("requests.get", new=fake_get):
        if expected != "error":
            assert count_dots_on_i("https://fake.com") == expected
        else:
            with pytest.raises(ValueError):
                count_dots_on_i("https://fake404.com")
