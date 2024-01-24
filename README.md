## reactpy-select

![](./docs/img/multi-select.png)

A minimal component wrapper for [react-select].
 
## Usage

    pip install reactpy-select

*[examples/simple_styles.py](examples/simple_styles.py)*
```
from reactpy import html, component, event, run, use_state
from reactpy_select import Select, ActionMeta, Options

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
            options=options
            ),

        html.h2(f"[{', '.join([v['value'] for v in values ])}]")
    )

```

### Supported Functionality

- [X] Current values
- [X] Custom styling
- [X] Default values
- [X] IsClearable, isDisabled, isSearchable
- [X] Multi-select
- [X] OnChange events
- [X] Placeholder
- [X] Themes


### [Custom Styling]

[react-select] uses a Javascript callback mechanism to allow the component style to be 
customized. All aspects of the select component can be customized. 

See [Adjusting the Styling] on the [react-select] website for examples. In reactpy
the javascript is wrapped in a multi-line python string. Javascript code can
be pasted into the string without modification.

```
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

    Select(
        ...
        styles=STYLES,
        )

```

[Adjusting the Styling]: https://react-select.com/components#adjusting-the-styling
[Dash Core Components]: https://dash.plotly.com/dash-core-components
[Plotly/Dash]: https://dash.plotly.com/
[react-select]: https://react-select.com/home
[dcc.Dropdown]: https://dash.plotly.com/dash-core-components/dropdown