from reactpy import html, component, event, run

from reactpy_select import Dropdown, EventActions, EventOptions

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]


@component
def AppMain():

    @event
    def onChange(event: EventOptions, action: EventActions):
        print(f"OnChange event={event} action={action['action']}")

    return html.div(
        html.h2('Dropdown Example'),
        Dropdown(options=options, multi=True, onchange=onChange)
    )

# python usage.py

if __name__ == "__main__":
    run(AppMain)

