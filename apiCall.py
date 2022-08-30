from alpha_vantage.timeseries import TimeSeries 
import time
import requests
import json 
from pandas import json_normalize
import pandas as pd

def earnings(key, list_of_tickers, output_path): 
    """ 
    key - API key from aplhavantage
    list_of_tickers = [] list only 
    
    return dataframe
    """
    # counter
    i = 0
    # empty datafraame
    df2 = pd.DataFrame()


    for ticker in list_of_tickers:
        i = i + 1 
        url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol={}&apikey={}'.format(ticker, key)

        # request fn our URL string is passed here 
        response = requests.get(url)
        
        # dumping all data into python object 
        response_dict = response.json()
        #  5 calls per minute and 500 calls per day cooldown charge you monthly on finaical data
        
        if i % 4 == 0:
            print("waiting ...")
            time.sleep(60)
        
        # type check make sure its a dict 
        print(type(response_dict))

        try:
            # you take headers of dictionary and state its header'
            # extracting list object
            selected_json = response_dict['quarterlyEarnings']
        except:
            print("Didnt data save", ticker)
            continue
        
        if isinstance(selected_json, list):
            pass
        try:
            selected_json = response_dict['quarterlyEarnings']
        except:
            # _, header= response.json()
            # print(_)
            # print(header)
            print("Didnt data save", ticker)
            continue

        # python list selected json into pandas dataframe insert database do dynamic serverless function 
        df = pd.DataFrame(selected_json)
        df.to_csv(output_path + 'file_quarterlyEarnings_{}.csv'.format(str(ticker)))
    
    return print("succesful query from API alpha vantage")



