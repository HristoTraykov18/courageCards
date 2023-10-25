
import pytest
from courage_cards import contains_valid_data


def test_invalid_start_event(data_frame):
    data_frame.replace(data_frame['event'].iloc[0], 'invalid', inplace=True)

    with pytest.raises(SystemExit) as wrapper_exc:
        contains_valid_data(data_frame)

    assert wrapper_exc.type == SystemExit
    assert wrapper_exc.value.code == 3


def test_too_many_start_events(data_frame):
    print(data_frame['event'].iloc[1])
    data_frame['event'].replace(
        data_frame['event'].iloc[1], 'start', inplace=True)
    print(data_frame['event'].iloc[1])
    print(data_frame['event'].iloc[0])

    with pytest.raises(SystemExit) as wrapper_exc:
        contains_valid_data(data_frame)

    assert wrapper_exc.type == SystemExit
    assert wrapper_exc.value.code == 4


def test_invalid_end_event(data_frame):
    data_frame.replace(data_frame['event'].iloc[-1], 'invalid', inplace=True)

    with pytest.raises(SystemExit) as wrapper_exc:
        contains_valid_data(data_frame)

    assert wrapper_exc.type == SystemExit
    assert wrapper_exc.value.code == 3


def test_too_many_end_events(data_frame):
    data_frame.replace(data_frame['event'].iloc[1], 'end', inplace=True)

    with pytest.raises(SystemExit) as wrapper_exc:
        contains_valid_data(data_frame)

    assert wrapper_exc.type == SystemExit
    assert wrapper_exc.value.code == 4
