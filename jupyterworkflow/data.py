import os
from urllib.request import urlretrieve
import pandas as pd


FREEMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Freemont.csv', url=FREEMONT_URL, force_download=False):
    """ Download and cache the frreemont data
   
    Parameters
    ----------
    filename : string (optional) 
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redoanload

    Returns
    -------
    data : pandas.DataFrame
        the freemont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Freemont.csv', index_col=('Date'), parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
