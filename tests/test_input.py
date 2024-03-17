import pandas as pd
import pytest
from app.io.input import read_file_builtin, read_file_pandas


def test_read_file_builtin_normal():
    result = read_file_builtin("./resources/existing_file.txt")
    assert result is not None, "Should not be None for existing files"
    assert isinstance(result, list), "Should return a list for existing files"
    assert len(result) == 1, "Should return a list with the correct number of lines for existing files"
    assert result[0] == "Test", "Should return the correct content for existing files"


def test_read_file_builtin_empty():
    result = read_file_builtin("./resources/empty.txt")
    assert result is not None, "Should not be None for empty existing files"
    assert isinstance(result, list), "Should return a list for empty files"
    assert len(result) == 0, "Should return an empty list for empty files"


def test_read_file_builtin_non_existing():
    with pytest.raises(RuntimeError, match="File not found"):
        read_file_builtin("./resources/non_existing_file.txt")


def test_read_file_pandas_normal():
    result = read_file_pandas("./resources/pandas.csv")
    assert isinstance(result, pd.DataFrame), "Should return a DataFrame for existing files"
    assert result.shape == (2, 3), "Should return a DataFrame with the correct shape for existing files"


def test_read_file_pandas_empty():
    with pytest.raises(RuntimeError, match="File not found or empty"):
        read_file_pandas("./resources/empty.txt")


def test_read_file_pandas_non_existing():
    with pytest.raises(RuntimeError, match="File not found or empty"):
        read_file_pandas("./resources/non_existing_file.txt")
