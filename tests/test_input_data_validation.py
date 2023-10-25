
import pytest
import courage_cards
import pandas as pd


@pytest.fixture
def data_frame():
    return pd.read_json("test_level_data.json")


def test_input_data_validation():
    df = data_frame

    assert courage_cards.contains_valid_data(df) is True
