import datetime
import os

import pytest
from conftest import TEST_FILES

import usercfgopt


@pytest.mark.parametrize("filename", os.listdir(TEST_FILES))
def test_file_parser(filename: str) -> None:
    # ensure file can be loaded
    with open(os.path.join(TEST_FILES, filename), "rb") as fp:
        original_data = usercfgopt.load(fp)

    # dump data to string
    dumped_data = usercfgopt.dumps(original_data)

    # load dumped data
    loaded_data = usercfgopt.loads(dumped_data)

    # ensure data is the same
    assert original_data == loaded_data


def test_fail_on_boolean() -> None:
    with pytest.raises(ValueError):
        usercfgopt.dumps({"key": True})


def test_fail_on_string_with_quote() -> None:
    with pytest.raises(ValueError):
        usercfgopt.dumps({"key": 'value with "quote"'})


def test_fail_on_object() -> None:
    with pytest.raises(ValueError):
        usercfgopt.dumps({"key": datetime.datetime.now()})
