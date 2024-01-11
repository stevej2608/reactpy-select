from reactpy import html, component, event, run

from reactpy_select import Dropdown

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]


@component
def AppMain():
    return html.div(
        html.h2('Dropdown Example'),
        Dropdown(options=options, multi=True)
    )

# python usage.py

if __name__ == "__main__":
    run(AppMain)

