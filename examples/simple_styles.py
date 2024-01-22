from reactpy import html, component, event, run

from reactpy_select.dropdown import Dropdown, ActionMeta, Options

# https://blog.logrocket.com/getting-started-react-select/#adding-custom-styles-react-select-components


options = [
  { 'value': 'vanilla', 'label': 'Vanilla', 'rating': 'safe' },
  { 'value': 'chocolate', 'label': 'Chocolate', 'rating': 'good' },
  { 'value': 'strawberry', 'label': 'Strawberry', 'rating': 'wild', 'isDisabled': True},
  { 'value': 'salted-caramel', 'label': 'Salted Caramel', 'rating': 'crazy' },
  { 'value': 'pistachio', 'label': 'Pistachio', 'rating': 'crazy' },
  { 'value': 'mint-chocolate-chip', 'label': 'Mint chocolate chip', 'rating': 'crazy' },
]

# STYLES = {
#     'option': {
#       'color': "#fff",
#       'backgroundColor': "#212529",

#       # isSelected: {
#       #   color: "#212529",
#       #   backgroundColor: "#a0a0a0"
#       # }
#     },

#     'control': {
#       'backgroundColor': "#212529",
#       'padding': "10px",
#       'border': "none",
#       'boxShadow': "none",
#     },

#     'singleValue': { 
#       'color': "#fff" 
#       },
#   }


STYLES = """
  {
    option: (defaultStyles, state) => ({
      ...defaultStyles,
      color: state.isSelected ? "#212529" : "#fff",
      backgroundColor: state.isSelected ? "#a0a0a0" : "#212529",
    }),

    control: (defaultStyles) => ({
      ...defaultStyles,
      backgroundColor: "#212529",
      padding: "10px",
      border: "none",
      boxShadow: "none",
    }),

    singleValue: (defaultStyles) => ({ ...defaultStyles, color: "#fff" }),
  };
"""


@component
def AppMain():

    @event
    def onChange(newValue: Options, actionMeta: ActionMeta):
        print(f"OnChange event={newValue} action={actionMeta['action']}")

    return html.div(
        html.h2('Dropdown Example (Styles)'),
        Dropdown(
            default_value=[options[0], options[1]],
            multi=True,
            name="flavours",
            onchange=onChange,
            options=options,
            class_name="basic-multi-select",
            class_name_prefix="select",
            styles=STYLES,
            id="dd1"
            )
    )

# python -m examples.simple_styles

if __name__ == "__main__":
    run(AppMain)
