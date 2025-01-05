# import pytest
from mython.grepy import grep_pattern_from_stdin


def test_grep_pattern_from_stdin():
    lines = ["hoge123", "fugaABC"]
    assert grep_pattern_from_stdin("g", lines) == [
        "ho\033[31mg\033[0me123",
        "fu\033[31mg\033[0maABC",
    ]
    assert grep_pattern_from_stdin("[1-9]+", lines) == ["hoge\033[31m123\033[0m"]
