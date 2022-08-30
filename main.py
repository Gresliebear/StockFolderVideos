
from re import A



# provide a ticker to the url API
# provide a key 
# provide a outpath/ serverless request / save database 

# import pandas lib as pd
import pandas as pd
#  pip install openpyxl

# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('SteelIndustry.xlsx')
print(dataframe1)
list_of_tickers = dataframe1['Ticker'].to_numpy()

# API call 
key = 'D03VFL5XJ25QWELA'
pathway = r'E:\StockFolder\outputfolder/' 

# create for url and pass those value
from apiCall import earnings

# pass out key parameter
# pass our list_of_tickers
#output data 

earnings(key, list_of_tickers, pathway)
