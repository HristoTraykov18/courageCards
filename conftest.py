
import pandas as pd
import pytest


@pytest.fixture
def data_frame():
    df = pd.read_json('test_level_data.json')
    yield df.copy()
