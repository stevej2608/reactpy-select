from reactpy import html, component, event, run

from reactpy_select.select import Select, ActionMeta, Options

# https://react-select.com/styles#overriding-the-theme
# https://codesandbox.io/p/sandbox/codesandboxer-example-rx8xjs?file=%2Fdocs%2Fdata.ts%3A11%2C53-11%2C69

options = [
  { 'value': 'vanilla', 'label': 'Vanilla', 'rating': 'safe' },
  { 'value': 'chocolate', 'label': 'Chocolate', 'rating': 'good' },
  { 'value': 'strawberry', 'label': 'Strawberry', 'rating': 'wild', 'isDisabled': True},
  { 'value': 'salted-caramel', 'label': 'Salted Caramel', 'rating': 'crazy' },
  { 'value': 'pistachio', 'label': 'Pistachio', 'rating': 'crazy' },
  { 'value': 'mint-chocolate-chip', 'label': 'Mint chocolate chip', 'rating': 'crazy' },
]

theme = {
  "borderRadius": 0,
  "colors": {
    "primary25": "hotpink",
    "primary": "black"
  }
}


@component
def AppMain():

    @event
    def onChange(newValue: Options, actionMeta: ActionMeta):
        print(f"OnChange event={newValue} action={actionMeta['action']}")

    return html.div(
        html.h2('Dropdown Example (Theme)'),
        Select(
            value=[options[0], options[1]],
            multi=True,
            onchange=onChange,
            options=options,
            theme=theme
            )
    )

# python -m examples.simple_theme

if __name__ == "__main__":
    run(AppMain)
