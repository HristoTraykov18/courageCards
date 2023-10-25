
from courage_cards import contains_valid_data


def test_valid_input_data(data_frame):
    i = tuple(data_frame['created'].keys()).index(416)
    data_frame['created'].replace(
        data_frame['created'].iloc[i], '2023-04-08 06:16:04.000000-07:00', inplace=True)

    assert contains_valid_data(data_frame) is True
