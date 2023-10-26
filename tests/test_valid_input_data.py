
from courage_cards import contains_valid_data


def test_valid_input_data(data_frame):
    assert contains_valid_data(data_frame) is True
