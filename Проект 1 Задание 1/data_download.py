import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker( ticker )
    data = stock.history( period=period )
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling( window=window_size ).mean()
    return data


def calculate_and_display_average_price(data):
    average = sum( data['Close'] ) / len( data['Close'] )
    print( f" Сумма значений за период = {sum( data['Close'] )}, количество значений= {len( data['Close'] )}, среднее "
           f'значение = {average}' )


def notify_if_strong_fluctuations(data, threshold):
    maximum = max( data['Close'] )
    minimum = min( data['Close'] )
    difference = round( (maximum - minimum) / minimum * 100, 2 )
    if difference > int( threshold ):
        print( f" Разница между max и min ценой составляет {difference} % от min цены, что превышает заданный порг в {threshold} %" )
