import yfinance as yf


# import talib as ta
# import pandas_ta as pta


def fetch_stock_data(ticker, period, start_date, end_date, my_interval="1d"):
    stock = yf.Ticker(ticker)
    if period != '':
        data = stock.history(period=period)
    else:
        data = stock.history(start=start_date, end=end_date, interval=my_interval)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """ Вывод средней цены за период. """
    if len(data['Close']) > 0:
        average = sum(data['Close']) / len(data['Close'])
        print(
            f" Сумма значений за период = {sum(data['Close'])}, количество значений= {len(data['Close'])}, среднее "
            f'значение = {average}')
    else:
        print('Нет данных')


def notify_if_strong_fluctuations(data, threshold):
    """ Функция уведомление о сильных колебаниях. """
    maximum = max(data['Close'])
    minimum = min(data['Close'])
    difference = round((maximum - minimum) / minimum * 100, 2)
    if difference > int(threshold):
        print(
            f" Разница между max и min ценой составляет {difference} % от min цены, что превышает заданный порг в {threshold} %")


def add_rsi_calculate(data, periods=5):
    """ Добавление RSI в dataset  """

    close_delta = data['Close'].diff()
    # Делаем две серий: одну для низких закрытий и одну для высоких закрытий
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    # Используем простую скользящую среднюю
    ma_up = up.rolling(window=periods).mean()
    ma_down = down.rolling(window=periods).mean()
    rsi = ma_up / ma_down
    rsi = 100 - (100 / (1 + rsi))
    data['RSI'] = rsi


def add_macd_calculate(data, fast=None, slow=None, signal=None, offset=None, **kwargs):
    """ Добавление MACD в dataset  """

    # Получаем 26-дневную EMA цены закрытия
    k = data['Close'].ewm(span=12, adjust=False, min_periods=12).mean()
    # Получаем 12-дневную EMA цены закрытия
    d = data['Close'].ewm(span=26, adjust=False, min_periods=26).mean()
    # Вычитаем 26-дневную EMA из 12-дневной EMA, чтобы получить MACD
    macd = k - d
    data['MACD'] = data.index.map(macd)
    # Получаем 9-дневную EMA MACD для линии срабатывания
    macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
    # Рассчитаем разницу между MACD - Триггером для значения Конвергенции/Дивергенции
    macd_h = macd - macd_s
    data['MACD_H'] = data.index.map(macd_h)
    data['MACD_S'] = data.index.map(macd_s)


def add_std_val_calculate(data, window_size=5):
    """ Добавление STD_VAL стандартного отклонения в dataset  """
    print(len(data['Close']))
    average = sum(data['Close']) / len(data['Close'])
    #    data['STD_VAL2'] = ((data['Close']-average) ** 2) ** 0.5
    data['STD_VAL'] = (((data['Close'] - average) ** 2) ** 0.5).rolling(window=window_size).mean()


def add_bollinger_calculate(data):
    """ Добавление линий Болльнджера в dataset  """
    average = sum(data['Close']) / len(data['Close'])
    data['BB_high'] = data['Moving_Average'] + 2 * data['STD_VAL']
    data['BB_low'] = data['Moving_Average'] - 2 * data['STD_VAL']
