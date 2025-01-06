Документация проекта для анализа и визуализации данных об акциях

Общий обзор

Этот проект предназначен для загрузки исторических данных об акциях и их визуализации. 
Он использует библиотеку yfinance для получения данных и matplotlib для создания графиков. 
Пользователи могут выбирать различные тикеры и временные периоды для анализа, а также просматривать движение цен и скользящие средние на графике.

Структура и модули проекта

1. data_download.py:

- Отвечает за загрузку данных об акциях.

- Содержит функции для извлечения данных об акциях из интернета и расчёта скользящего среднего, вычисления среднего значения цены закрытия, уведомления о превышении порогового значения изменения цены.


2. main.py:

- Является точкой входа в программу.

- Запрашивает у пользователя тикер акции и временной период, пороговое значение в % для анализа сильных колебаниях, загружает данные, обрабатывает их и выводит результаты в виде графика.



3. data_plotting.py:

- Отвечает за визуализацию данных.

- Содержит функции для создания и сохранения графиков цен закрытия и скользящих средних.



Описание функций



1. data_download.py:

- fetch_stock_data(ticker, period): Получает исторические данные об акциях для указанного тикера и временного периода. Возвращает DataFrame с данными.

- add_moving_average(data, window_size): Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.



2. main.py:

- main(): Основная функция, управляющая процессом загрузки, обработки данных и их визуализации. Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных, а затем передаёт результаты на визуализацию.



3. data_plotting.py:

- create_and_save_plot(data, ticker, period, filename): Создаёт график, отображающий цены закрытия и скользящие средние. Предоставляет возможность сохранения графика в файл. Параметр filename опционален; если он не указан, имя файла генерируется автоматически.



Пошаговое использование

1. Запустите main.py.

2. Введите интересующий вас тикер акции (например, 'AAPL' для Apple Inc).

3. Введите желаемый временной период для анализа (например, '1mo' для данных за один месяц).

4. Введите пороговое значение (в %) для уведомления о сильных колебаниях цены

5. Программа обработает введённые данные, загрузит соответствующие данные об акциях, рассчитает скользящее среднее выведет среднее значение цены, выдаст уведомление если изменение цены превышает заданное пороговое значение и отобразит график


Задания нацелены на улучшение пользовательского опыта и расширение аналитических возможностей проекта, предоставляя глубокие и настраиваемые инструменты для анализа данных об акциях.

Пример графика
![image](https://github.com/user-attachments/assets/47ffb689-98a7-4cb8-b8bf-47eec46737a2)

