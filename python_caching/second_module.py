from datetime import datetime

import pandas as pd


def set_current_date(data: pd.DataFrame) -> pd.DataFrame:
    data["date"] = datetime.today()
    return data
