from typing import List, Dict, Union
import json
import requests
import pandas as pd

def get_data(endpoint:str, url:str="http://localhost:8000", ext=None)->Union[List, Dict]:
    """Call api to get data

    Args:
        url (str): base url
        endpoint (str): api endpoint
        ext (str|int, optional): extension to the endpoint. Defaults to None.

    Returns:
        Union[List, Dict]: _description_
    """
    url = f"{url}/{endpoint}/"
    if ext:
        url = f"{url}{ext}/"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def read_api_df_filter_year(filter:Union[str, int])->pd.DataFrame:
    """ Read api data into dataframe and filter by year
    Args:
        filter (Union[str, int]): A value to filter the data by

    Returns:
        pd.DataFrame: Pandas dataframe
    """

    response = get_data("mortgages")
    # res = response.json()
    df = pd.json_normalize(response)
    df['created'] = pd.to_datetime(df['created'])
    if filter == 'All':
        return df
    else:
        return df[df['created'].dt.year == filter]


def create_payment(
        payload:Dict[str, Union[str, Union[float, int]]], 
        url:str="http://localhost:8000"
        )->Dict[str, Union[float, int]]:
    """ Create a new payment
    Args:
        url (str): base url
        payload (Dict[str, Union[str, Union[float, int]]]): payload to send to the api
    """
    url = f"{url}/mortgages/"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, params=payload, headers=headers)
    response.raise_for_status()

    return response.json()

