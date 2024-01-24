import sys
from io import StringIO
import plotly.graph_objects as go
import pandas as pd
import colorlover as cl
from reactpy import html, component, event, use_state, utils
from reactpy_select.dropdown import Dropdown, ActionMeta, Options


from utils.fast_server import run
from utils.options import ServerOptions

PLOTLY_JS = html.script({
    'src': 'https://cdn.plot.ly/plotly-latest.min.js',
    'charset': 'utf-8'
})


try:
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/dash-stock-ticker-demo.csv')
except Exception:
    print("Unable to read 'dash-stock-ticker-demo.csv' from github, no internet connection?")
    sys.exit(0)

colorscale = cl.scales['9']['qual']['Paired']

def bbands(price, window_size=10, num_of_std=5):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std*num_of_std)
    lower_band = rolling_mean - (rolling_std*num_of_std)
    return rolling_mean, upper_band, lower_band


def update_graph(tickers=None):
    tickers = tickers or []
    graphs = []

    if not tickers:
        graphs.append(html.h2({'style': {'marginTop': 20, 'marginBottom': 20}}, "Select a stock ticker."))
    else:
        for i, ticker in enumerate(tickers):

            dff = df[df['Stock'] == ticker]

            candlestick = {
                'x': dff['Date'],
                'open': dff['Open'],
                'high': dff['High'],
                'low': dff['Low'],
                'close': dff['Close'],
                'type': 'candlestick',
                'name': ticker,
                'legendgroup': ticker,
                'increasing': {'line': {'color': colorscale[0]}},
                'decreasing': {'line': {'color': colorscale[1]}}
            }
            bb_bands = bbands(dff.Close)
            bollinger_traces = [{
                'x': dff['Date'], 'y': y,
                'type': 'scatter', 'mode': 'lines',
                'line': {'width': 1, 'color': colorscale[(i*2) % len(colorscale)]},
                'hoverinfo': 'none',
                'legendgroup': ticker,
                'showlegend': (i == 0),
                'name': f'{ticker} - bollinger bands'
            } for i, y in enumerate(bb_bands)]

            # https://plotly.com/python-api-reference/generated/plotly.express.line
            # https://plotly.com/python/line-charts/
            # https://plotly.com/python/candlestick-charts/
            # https://plotly.com/python/range-slider/

            # fig = px.line(
            #     [candlestick] + bollinger_traces,
            #     orientation='h',
            #     width=600,
            #     height=400,
            #     title='Line Chart'
            # )

            # https://plotly.com/python/candlestick-charts/

            fig = go.Figure(data=[
                        go.Line(bollinger_traces[0]),
                        go.Line(bollinger_traces[1]),
                        go.Line(bollinger_traces[2]),
                        go.Candlestick(candlestick)
                    ])


            # Create an html object in memory from fig.

            buffer = StringIO()
            fig.write_html(buffer, include_plotlyjs='cdn')
            fig_html = buffer.getvalue()

            graphs.append(utils.html_to_vdom(fig_html))
            graphs.append(html.br())

    return html.div(graphs)


@component
def AppMain():

    values, set_values =  use_state([])

    tickers=[{'label': s[0], 'value': str(s[1])}
                for s in zip(df.Stock.unique(), df.Stock.unique())]

    @event
    def on_change(selectedTickers: ServerOptions, actionMeta: ActionMeta):
        set_values(selectedTickers)


    return html.div(
        html.h2('Finance Explorer'),
        html.br(),
        Dropdown(
            default_value=values,
            onchange=on_change,
            options=tickers,
            multi=True
            ),
        html.br(),
        html.div({'id': 'graphs'}, update_graph([val['value'] for val in values]))
    )

# python -m examples.dash_ticker_example


if __name__ == '__main__':
    options = ServerOptions(head=[PLOTLY_JS])
    run(AppMain, options=options)
