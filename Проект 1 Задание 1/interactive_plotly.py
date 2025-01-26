import pandas as pd
import matplotlib.pyplot as plt
import datetime

import plotly
import plotly.graph_objects as go


def create_and_save_int_plot2(data, ticker, period, stl):
    if pd.api.types.is_datetime64_any_dtype(data.index):
        dates = data.index.to_numpy()
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            mode='lines+markers',  # линии и точки
            x=dates, y=data['Close'],  # данные
            name='AAPL-Close',  # имя в легенде
            marker=dict(color='#00CC66', size=7),  # цвет в html-формате
            opacity=0.8,  # прозрачность
            line={'width': 3})  # свойства линии - толщина
        )

        fig.add_trace(go.Scatter(
            x=dates, y=data['Moving_Average'],  # данные
            name='Moving_Average',  # имя в легенде
            marker=dict(  # свойства маркера
                color='rgba(255,48,0,1)',  # цвет в rgb-формате
                size=7  # размер маркера
            ),  # цвет в html-формате
            opacity=0.8,  # прозрачность
            line={'width': 3})  # свойства линии - толщина
        )
        fig.add_trace(go.Scatter(
            x=dates, y=data['BB_high'],  # данные
            name='Bollinger_high',  # имя в легенде
            marker=dict(  # свойства маркера
                color='red',  # цвет в rgb-формате
                size=17  # размер маркера
            ),  # цвет в html-формате
            opacity=0.8,  # прозрачность
            line={'width': 3})  # свойства линии - толщина
        )
        fig.add_trace(go.Scatter(
            x=dates, y=data['BB_low'],  # данные
            name='Bollinger_low',  # имя в легенде
            marker=dict(  # свойства маркера
                color='red',  # цвет в rgb-формате
                size=7  # размер маркера
            ),  # цвет в html-формате
            opacity=0.8,  # прозрачность
            line={'width': 3})  # свойства линии - толщина
        )
        # свойства фигуры
        fig.update_layout(
            height=650, width=1100,  # размер фигуры
            title_text='AAPL',  # заголовок графика
            yaxis_title='Стоимость',
            title_font_size=16,  # размер заголовка
            plot_bgcolor='rgba(0,0,0,0.05)',  # цвет фона
            xaxis_rangeslider_visible=True  # слайдер
        )

        # параметры оси абсцисс
        fig.update_xaxes(
            # range=[-1.5, 1.5],  # ограничение графика
            zeroline=True,  # рисовать линию x=0
            zerolinewidth=2  # толщина линии x=0
        )

        # параметры оси ординат
        fig.update_yaxes(
            zeroline=True,  # рисовать линию y=0
            zerolinewidth=2,  # толщина линии y=0
            zerolinecolor='LightGray'  # цвет линии y=0
        )

        # показать график
        fig.show()
        plotly.offline.plot(fig, filename='example.html', auto_open=False)
