import datetime
import os

import pytest

import usercfg_opt_parser
from tests.conftest import TEST_FILES


@pytest.mark.parametrize("filename", os.listdir(TEST_FILES))
def test_file_parser(filename: str) -> None:
    # ensure file can be loaded
    with open(os.path.join(TEST_FILES, filename), "rb") as fp:
        original_data = usercfg_opt_parser.load(fp)

    # dump data to string
    dumped_data = usercfg_opt_parser.dumps(original_data)

    # load dumped data
    loaded_data = usercfg_opt_parser.loads(dumped_data)

    # ensure data is the same
    assert original_data == loaded_data


def test_fail_on_boolean() -> None:
    with pytest.raises(ValueError):
        usercfg_opt_parser.dumps({"key": True})


def test_fail_on_string_with_quote() -> None:
    with pytest.raises(ValueError):
        usercfg_opt_parser.dumps({"key": 'value with "quote"'})


def test_fail_on_object() -> None:
    with pytest.raises(ValueError):
        usercfg_opt_parser.dumps({"key": datetime.datetime.now()})
