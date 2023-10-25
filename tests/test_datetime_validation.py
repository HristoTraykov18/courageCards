
import pytest

from courage_cards import contains_valid_data


def test_invalid_datetime_format(data_frame):
    with pytest.raises(SystemExit) as wrapper_exc:
        contains_valid_data(data_frame)

    assert wrapper_exc.type == SystemExit
    assert wrapper_exc.value.code == 5


def test_invalid_date_created(data_frame):
    i = tuple(data_frame['created'].keys()).index(416)
    data_frame['created'].replace(
        data_frame['created'].iloc[i], '2023-03-08 06:16:04.000000-07:00', inplace=True)

    with pytest.raises(SystemExit) as wrapper_exc:
        contains_valid_data(data_frame)

    assert wrapper_exc.type == SystemExit
    assert wrapper_exc.value.code == 6
