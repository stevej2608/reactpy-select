from reactpy import html, component, event, run
from reactpy_select.select import Select, ActionMeta, Options

# Python clone of one of the more complex react-select
# custom style examples.
#
# See https://react-select.com/home#custom-styles

colourOptions = [
    {'value': 'ocean', 'label': 'Ocean', 'color': '#00B8D9', 'isFixed': True},
    {'value': 'blue', 'label': 'Blue', 'color': '#0052CC', 'isDisabled': True},
    {'value': 'purple', 'label': 'Purple', 'color': '#5243AA'},
    {'value': 'red', 'label': 'Red', 'color': '#FF5630', 'isFixed': True},
    {'value': 'orange', 'label': 'Orange', 'color': '#FF8B00'},
    {'value': 'yellow', 'label': 'Yellow', 'color': '#FFC400'},
    {'value': 'green', 'label': 'Green', 'color': '#36B37E'},
    {'value': 'forest', 'label': 'Forest', 'color': '#00875A'},
    {'value': 'slate', 'label': 'Slate', 'color': '#253858'},
    {'value': 'silver', 'label': 'Silver', 'color': '#666666'},
]

colourStyles = {
    'control': '''(styles) => ({ ...styles, backgroundColor: 'white' })''',

    'option': '''(styles, { data, isDisabled, isFocused, isSelected }) => {
      const color = chroma(data.color);
      return {
        ...styles,
        backgroundColor: isDisabled
          ? undefined
          : isSelected
            ? data.color
            : isFocused
              ? color.alpha(0.1).css()
              : undefined,
        color: isDisabled
          ? '#ccc'
          : isSelected
            ? chroma.contrast(color, 'white') > 2
              ? 'white'
              : 'black'
            : data.color,
        cursor: isDisabled ? 'not-allowed' : 'default',

        ':active': {
          ...styles[':active'],
          backgroundColor: !isDisabled
            ? isSelected
              ? data.color
              : color.alpha(0.3).css()
            : undefined,
        },
      }
    }''',

  'multiValue': '''(styles, { data }) => {
    const color = chroma(data.color);
    return {
      ...styles,
      backgroundColor: color.alpha(0.1).css(),
    }
  }''',

  'multiValueLabel': '''(styles, { data }) => {
    return {
      ...styles,
      color: data.color
    }
  }''',

  'multiValueRemove': '''(styles, { data }) => ({
    ...styles,
    color: data.color,
    ':hover': {
      backgroundColor: data.color,
      color: 'white',
      },
  })''',
}


@component
def AppMain():

    @event
    def onChange(newValue: Options, actionMeta: ActionMeta):
        print(f"OnChange event={newValue} action={actionMeta['action']}")

    return html.div(
        html.h2('Multi Select Example (Styles)'),
        Select(
            close_menu_onselect=False,
            default_value=[colourOptions[0], colourOptions[1]],
            multi=True,
            onchange=onChange,
            options=colourOptions,
            styles=colourStyles,
            )
    )

# python -m examples.multi_select_example

if __name__ == '__main__':
    run(AppMain)
