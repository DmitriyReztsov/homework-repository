from unittest import mock

from pytest import fixture

TEXT_1 = (
    "qwertyuiop asdfghjkl \n"
    "zxcvbnm FFF\u00e4lle\n"
    "poiuytrewq \n"
    "lkjhgfdsa \n"
    "mnbvcxz \n"
    "1234567890 1234567890 1234567890 \n"
    "qqqqqqqqqq \n"
    "aaaaaaaaaa \n"
    "qqwwqqwwqw \n"
    "as qw re fds zxc re rtry vc ss \u00e4\n"
    "\u2014 ! - ,"
)


@fixture()
def open_file():
    read_data = TEXT_1
    return mock.mock_open(read_data=read_data)
