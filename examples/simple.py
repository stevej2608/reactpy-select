from reactpy import html, component, event, run

from reactpy_select.dropdown import Dropdown, ActionMeta, Options

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

@component
def AppMain():

    @event
    def onChange(newValue: Options, actionMeta: ActionMeta):
        print(f"OnChange event={newValue} action={actionMeta['action']}")

    return html.div(
        html.h2('Dropdown Example'),
        Dropdown(options=options, multi=True, onchange=onChange, id="dd1")
    )

# python -m examples.simple

if __name__ == "__main__":
    run(AppMain)
