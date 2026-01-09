from reactpy import html, component, event
from reactpy_select import Select, ActionMeta, Options
from utils.app_runner import AppRunner

options: Options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

@component
def AppMain():

    @event
    def on_change(newValue: Options, actionMeta: ActionMeta) -> None:
        print(f"OnChange event={newValue} action={actionMeta['action']}")


    return html.div(
        html.h2('Dropdown Example'),
        Select(options=options, onchange=on_change, id="dd1", class_name_prefix="react-select"),
    )

# python -m examples.simple

if __name__ == "__main__":
    AppRunner.run(AppMain)
