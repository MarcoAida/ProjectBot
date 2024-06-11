#Using Dash:

from dash import Dash, dcc, html
import plotly.graph_objs as go


def create_dash_app(server, df):
    app = Dash(server=server, routes_pathname_prefix='/dash/')

    app.layout = html.Div(children=[
        html.H1(children='Cryptocurrency Trading Dashboard'),
        dcc.Graph(id='price-chart',
                  figure={
                      'data': [
                          go.Candlestick(x=df.index,
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'],
                                         name='Candlestick Chart')
                      ],
                      'layout': {
                          'title': 'Price Chart'
                      }
                  }),
        dcc.Graph(
            id='sma-chart',
            figure={
                'data': [
                    go.Scatter(
                        x=df.index, y=df['SMA50'], mode='lines', name='SMA50'),
                    go.Scatter(x=df.index,
                               y=df['SMA200'],
                               mode='lines',
                               name='SMA200')
                ],
                'layout': {
                    'title': 'Moving Averages'
                }
            })
    ])

    return app
