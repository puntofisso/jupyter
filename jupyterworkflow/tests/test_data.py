#pytest: providing file is called test_XXXXXX it works
from jupyterworkflow.data import get_fremont_data
import pandas as pd
import numpy as np
def test_fremont_data():
    data = get_fremont_data()
    # we want to make sure the output is good
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)
