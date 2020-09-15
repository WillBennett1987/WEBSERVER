from django.apps import AppConfig
from data_processing import get_stock_data_DF
from models import Stock_table

class ResearchConfig(AppConfig):
    name = 'research'

class ingestion_engine:#this is where we update the stock_table
    def __init__(self):
        pass

    def update_stock_table(self, stock_df, stock_sym):
        for key, index in enumerate(stock_df): #this will interate through the dictionary and give the index and the key 
            Stock_table.objects.create(
                Stock_Date=key,
                Stock_Sym=stock_sym,
                Stock_open=stock_df[key]['Open'],
                Stock_close=stock_df[key]['Close'],
                Stock_high=stock_df[key]['High'],
                Stock_low=stock_df[key]['Low']) # this creates a record of a stock event
            if index % 10 == 0:
                print(f'Date : {key} \n Sym : {stock_sym} \n Close : {stock_df[key]["Close"]}')

        print(Stock_table.objects.all())
    
    def add_stockdate(self, stock_sym):#this is for unit testing during development
        stock_df = get_stock_data_DF('AMZN')
        self.update_stock_table(stock_df, stock_sym)
        return stock_df

if __name__ == "__main__":
    x = ingestion_engine()
    x.add_stockdate('AMZN')
    
            
            