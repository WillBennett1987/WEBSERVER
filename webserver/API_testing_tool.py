import requests

def run_update_stockdata(stock_sym):
    url = '127.0.0.1:8000/api-data/'

    params = {
        'type' : 'update_stock_data',
        'stock_sym' : stock_sym,
    }

    response = requests.get(url, params)
    print(response)

if __name__ == '__main__':
    run_update_stockdata('AMZN')