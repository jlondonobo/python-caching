from datetime import datetime

import pandas as pd

from python_caching.second_module import set_current_date


def test_set_current_date():
    # create a sample dataframe
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]})

    result = set_current_date(data)
    assert "date" in result.columns
    assert all(dt.date() == datetime.today().date() for dt in result["date"])
