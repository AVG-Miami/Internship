import yfinance as yf
# import talib as ta
import pandas_ta as pta


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker( ticker )
    data = stock.history( period=period )
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling( window=window_size ).mean()
    return data


def calculate_and_display_average_price(data):
    """ Вывод средней цены за период. """
    if len( data['Close'] ) > 0:
        average = sum( data['Close'] ) / len( data['Close'] )
        print(
            f" Сумма значений за период = {sum( data['Close'] )}, количество значений= {len( data['Close'] )}, среднее "
            f'значение = {average}' )
    else:
        print( 'Нет данных' )


def notify_if_strong_fluctuations(data, threshold):
    """ Функция уведомление о сильных колебаниях. """
    maximum = max( data['Close'] )
    minimum = min( data['Close'] )
    difference = round( (maximum - minimum) / minimum * 100, 2 )
    if difference > int( threshold ):
        print(
            f" Разница между max и min ценой составляет {difference} % от min цены, что превышает заданный порг в {threshold} %" )


def add_rsi_calculate(data, window_size=5):
    """ Добавление RSI в dataset  """
    #    data['RSI'] = data['Close'].rolling( window=window_size ).mean()
    #    data['RSI'] = pta.rsi(data['Close'], length = len(data['Close']))

    periods = len( data['Close'] )
    close_delta = data['Close'].diff()
    # Делаем две серий: одну для низких закрытий и одну для высоких закрытий
    up = close_delta.clip( lower=0 )
    down = -1 * close_delta.clip( upper=0 )
    # Использование экспоненциальной скользящей средней
    # ma_up = up.ewm( com=periods - 1, adjust=True, min_periods=periods ).mean()
    # ma_down = down.ewm( com=periods - 1, adjust=True, min_periods=periods ).mean()
    # Использование простой скользящей средней
    ma_up = up.rolling( window=periods ).mean()
    ma_down = down.rolling( window=periods ).mean()

    print( 'ma_up' )
    print( ma_up )
    print( 'ma_down' )
    print( ma_down )
    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    print( 'RSI' )
    print( rsi )
    data['RSI'] = rsi


def add_macd_calculate(data, window_size=5):
    """ Добавление MACD в dataset  """
    #    data['RSI'] = data['Close'].rolling( window=window_size ).mean()
    data['MACD'] = pta.macd( data['Close'], length=len( data['Close'] ) )
    pass
