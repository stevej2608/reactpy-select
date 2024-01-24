from reactpy import html, component, event, run, use_state

from reactpy_select import Select, ActionMeta, Options

# https://blog.logrocket.com/getting-started-react-select/#adding-custom-styles-react-select-components

options = [
  { 'value': 'vanilla', 'label': 'Vanilla', 'rating': 'safe'},
  { 'value': 'chocolate', 'label': 'Chocolate', 'rating': 'good' },
  { 'value': 'strawberry', 'label': 'Strawberry', 'rating': 'wild', 'isDisabled': True},
  { 'value': 'salted-caramel', 'label': 'Salted Caramel', 'rating': 'crazy' },
  { 'value': 'pistachio', 'label': 'Pistachio', 'rating': 'crazy' },
  { 'value': 'mint-chocolate-chip', 'label': 'Mint chocolate chip', 'rating': 'crazy' },
]

STYLES = {
    'option': '''(defaultStyles, state) => ({
      ...defaultStyles,
      color: state.isSelected ? "#212529" : "#fff",
      backgroundColor: state.isSelected ? "#a0a0a0" : "#212529",
    })''',

    'control': '''(defaultStyles) => ({
      ...defaultStyles,
      backgroundColor: "#212529",
      padding: "10px",
      border: "none",
      boxShadow: "none",
    })''',

    'singleValue': '''(defaultStyles) => ({ ...defaultStyles, color: "#fff" })''',
  }


@component
def AppMain():
    values, set_values = use_state([])

    @event
    def on_change(new_value: Options, actionMeta: ActionMeta):
        set_values(new_value)

    return html.div(
        html.h2('Dropdown Example, default values (Custom styles)'),
        Select(
            value = values,
            default_value=[options[0], options[1]],
            multi=True,
            onchange=on_change,
            options=options,
            styles=STYLES,
            ),
        html.h2(f"[{', '.join([v['value'] for v in values ])}]")
    )

# python -m examples.simple_styles

if __name__ == "__main__":
    run(AppMain)
