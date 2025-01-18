import data_download as dd
import data_plotting as dplt


def main():
    print( "Добро пожаловать в инструмент получения и построения графиков биржевых данных." )
    print(
        "  А так же для вычисления средней цены за  период, и получения уведомления о сильных колебаниях первышающих " )
    print( "  первышающих заданый порог в % " )
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc),"
        " MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc)." )
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, "
        "с начала года, макс." )

    ticker = input( "Введите тикер акции (например, «AAPL» для Apple Inc):»" ).upper()
    period = input(
        "Введите период для данных (например, '1mo' для одного месяца) или нажмите 'Enter' для ввода периода: " )
    if period == '':
        start_date = input( "Введите дату начала периода в формате (2022-01-02) :" )
        end_date = input( "Введите дату конца периода в формате (2022-01-02) :" )
        interval = input( "Введите интервал (1d, 1mo) по умолчанию 1d :" )
    threshold = input( "Введите пороговое значение (в %) для уведомления о сильных колебаниях цены: " )
    f_name = input( "Введите имя файла для экспорта в CSV фаил :" )

    # Fetch stock data
    stock_data = dd.fetch_stock_data( ticker, period, start_date, end_date, interval )

    # Add moving average to the data
    stock_data = dd.add_moving_average( stock_data )

    # Add RSI to the data
    rsi_data = dd.add_rsi_calculate( stock_data )

    # Add MACD to the data
    macd_data = dd.add_macd_calculate( stock_data )

    #  Вывод средней цены за период
    dd.calculate_and_display_average_price( stock_data )

    # уведомление о сильных колебаниях
    dd.notify_if_strong_fluctuations( stock_data, threshold )

    # Plot the data
    graphic = dplt.create_and_save_plot( stock_data, ticker, period )

    # Экспорт в Exel
    dplt.export_data_to_exel( stock_data, ticker, graphic )

    # Экспорт в CSV фаил
    dplt.export_data_to_csv( stock_data, f_name )


if __name__ == "__main__":
    main()
