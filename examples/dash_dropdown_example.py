from reactpy import html, component, run
from reactpy_select import Select

# Mimic the style of the classic Plotly/Dash Stock Tickers Demo App
#
# See https://github.com/plotly/dash-stock-tickers-demo-app


TICKERS = [
    {'label': 'AAPL', 'value': 'AAPL'}, 
    {'label': 'TSLA', 'value': 'TSLA'}, 
    {'label': 'COKE', 'value': 'COKE'}, 
    {'label': 'YHOO', 'value': 'YHOO'}, 
    {'label': 'GOOGL', 'value': 'GOOGL'}
    ]

colourStyles = {

  'multiValueLabel': '''(styles, { data }) => ({
    ...styles,
    color: '#5ca3ff',
  })''',

  'multiValue': '''(styles, { data }) => {
    return {
      ...styles,
      backgroundColor: '#ebf5ff',
      border: '1px solid #c2e0ff'
    }
  }''',

  'multiValueRemove': '''(styles, { data }) => ({
    ...styles,
    color: '#5ca3ff',
    ':hover': {
      backgroundColor: '#d9ebfd',
    },
  })''',
}

@component
def AppMain():

    return html.div(
        html.h2('Dash Tickers Example (Custom Styles)'),
        Select(
            multi=True,
            options=TICKERS,
            styles=colourStyles,
            is_searchable = False
            )
    )

# python -m examples.dash_dropdown_example

if __name__ == '__main__':
    run(AppMain)
