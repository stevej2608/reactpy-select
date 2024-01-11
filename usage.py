from reactpy import html, component, event, run

from reactpy_select.dropdown import Dropdown, ActionMeta, EventOptions

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]


@component
def AppMain():

    @event
    def onChange(newValue: EventOptions, actionMeta: ActionMeta):
        print(actionMeta['xaction'])
        print(f"OnChange event={newValue} action={actionMeta['action']}")

    return html.div(
        html.h2('Dropdown Example'),
        Dropdown(options=options, multi=True, onchange=onChange, id="dd1")
    )

# python usage.py

if __name__ == "__main__":
    run(AppMain)
