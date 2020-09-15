import pandas_datareader as web
from requests import get
#import models
import json

def get_stock_data_DF(stock_sym, data_source='yahoo', start=None, end=None, columns=['High', 'Low', 'Close']): #this uses the pandas_datareader libary to get stock data for free. althouhg its a limited dataset
    stock_df = web.DataReader(stock_sym, data_source=data_source, start=start, end=end)#gets data in the form of a dataframe
    #stock_df = stock_df.filter(columns) #takes only the needed columns, some sources uses dates as index and i may need to make them a field.
    return stock_df

def get_stock_data_API(url, params): # i can't find an api at this current moment but i will keep this function for future uses
    response_data = get(url, params)
    stock_data = json.loads(response_data)
    return stock_data


if __name__ == "__main__": # will run this code if not imported
    print(get_stock_data_DF('AMZN'))