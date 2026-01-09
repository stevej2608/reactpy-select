import sys
from typing import List, Dict, Any, Tuple, cast, Union

from io import StringIO
import plotly.graph_objects as go
import pandas as pd
import colorlover as cl
from reactpy import html, component, event, use_state, utils
from reactpy.types import VdomDict

from reactpy_select import Select, ActionMeta, Options

from utils.app_runner import AppRunner
from utils.server_options import ServerOptions

from .dash_dropdown_example import colourStyles

# ReactPy clone of the classic Plotly/Dash Stock Tickers Demo App
#
# See https://github.com/plotly/dash-stock-tickers-demo-app
#
# Integration of plotly.graph_objects with ReactPy:
#
# See https://energybeam.blogspot.com/2023/08/how-to-add-plotly-charts-in-reactpy.html

PLOTLY_JS = 'https://cdn.plot.ly/plotly-latest.min.js'

try:
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/dash-stock-ticker-demo.csv') # type: ignore
except Exception:
    print("Unable to read 'dash-stock-ticker-demo.csv' from github, no internet connection?")
    sys.exit(0)

colorscale = cl.scales['9']['qual']['Paired']

def bbands(price: Any, window_size:int=10, num_of_std:int=5) -> Tuple[float, float, float]: # type: ignore

    rolling_mean: float = price.rolling(window=window_size).mean()
    rolling_std: float = price.rolling(window=window_size).std()
    upper_band: float = rolling_mean + (rolling_std*num_of_std)
    lower_band: float = rolling_mean - (rolling_std*num_of_std)

    return rolling_mean, upper_band, lower_band

def update_graph(tickers: Union[List[str], None]=None) -> VdomDict:
    tickers = tickers or []
    graphs: List[VdomDict] = []

    if not tickers:
        graphs.append(html.h2({'style': {'marginTop': 20, 'marginBottom': 20}}, "Select a stock ticker."))
    else:
        for _i, ticker in enumerate(tickers):

            dff: pd.DataFrame = df[df['Stock'] == ticker]  # type: ignore[assignment]

            candlestick:  Dict[str, Any] = {
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
            bb_bands = bbands(dff.Close) # type: ignore
            bollinger_traces: List[Dict[str, Any]]  = [{
                'x': dff['Date'], 'y': y,
                'mode': 'lines',
                'line': {'width': 2, 'color': colorscale[(i*2) % len(colorscale)]},
                'hoverinfo': 'none',
                'legendgroup': ticker,
                'showlegend': (i == 0),
                'name': f'{ticker} - Bollinger Bands'
            } for i, y in enumerate(bb_bands)]

            # https://plotly.com/python/candlestick-charts/

            fig: Any = go.Figure(data=[
                        *[go.Scatter(t) for t in bollinger_traces],
                        go.Candlestick(candlestick)
                    ])

            fig.update_layout(
                legend=dict(
                    bgcolor='White',
                    yanchor="top",
                    y=1.00,
                    xanchor="left",
                    x=0.00
                ),
                plot_bgcolor='rgba(0, 0, 0, 0)',
                paper_bgcolor='rgba(0, 0, 0, 0)',
                margin={'b': 0, 'r': 10, 'l': 60, 't': 20},
            )

            fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

            # Create an html object in memory from fig.

            buffer = StringIO()
            fig.write_html(buffer, include_plotlyjs='cdn', config={'displayModeBar': False})
            fig_html = buffer.getvalue()

            graphs.append(utils.string_to_reactpy(fig_html))

    return html.div(graphs)


@component
def AppMain():

    values, set_values =  use_state(cast(Options,[]))

    # pandas DataFrame types are not fully understood by pyright
    tickers: Options = [{'label': str(s[0]), 'value': str(s[1])}  # type: ignore[misc]
                for s in zip(df.Stock.unique(), df.Stock.unique())]  # type: ignore[misc]

    @event
    def on_change(selectedTickers: Options, actionMeta: ActionMeta):
        set_values(selectedTickers)

    return html.div(
        html.h2('Finance Explorer'),
        html.br(),
        Select(
            default_value = values,
            onchange=on_change,
            options=tickers,
            multi=True,
            styles=colourStyles
            ),
        html.div({'id': 'graphs'}, update_graph([val['value'] for val in values]))
    )

# python -m examples.dash_ticker_example

if __name__ == '__main__':
    title=html.title("Ticker Example")
    AppRunner.run(AppMain, additional_head=[PLOTLY_JS])
