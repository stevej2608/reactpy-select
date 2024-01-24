from typing import List, Dict, Callable, TypedDict, Literal, Optional
from .bundle_wrapper import _Select

# https://react-select.com/props
# https://dash.plotly.com/dash-core-components/dropdown#examples


Option = Dict[Literal["label", "value"], str]

ActionTypes = Literal[
    "clear",
    "create-option",
    "deselect-option",
    "pop-value",
    "remove-value",
    "select-option",
    "set-value",
]

Options = List[Option]

class ActionMeta(TypedDict):
    action: ActionTypes
    option: Optional[Options]

OnChangeEvent = Callable[[Options, ActionMeta], None]

# Theme customization, see:
#   https://react-select.com/styles#overriding-the-theme
#   https://github.com/JedWatson/react-select/blob/master/packages/react-select/src/theme.ts
#

def Select(
    options: Options,
    close_menu_onselect: Optional[bool] = True,
    class_name: Optional[str] = None,
    class_name_prefix: Optional[str] = None,
    default_value: Options = None,
    id: Optional[str] = None,
    multi: bool = False,
    name: Optional[str] = None,
    onchange: Optional[OnChangeEvent] = None,
    styles:  Optional[Dict] = None,
    theme:  Optional[Dict] = None,
    ):
    """ReactPy wrapper for react-select component

    Args:
        options (Options): _description_
        close_menu_onselect (Optional[bool], optional): _description_. Defaults to True.
        class_name (Optional[str], optional): _description_. Defaults to None.
        class_name_prefix (Optional[str], optional): _description_. Defaults to None.
        default_value (Options, optional): _description_. Defaults to None.
        id (Optional[str], optional): _description_. Defaults to None.
        multi (bool, optional): _description_. Defaults to False.
        name (Optional[str], optional): _description_. Defaults to None.
        onchange (Optional[OnChangeEvent], optional): _description_. Defaults to None.
        styles (Optional[Dict], optional): _description_. Defaults to None.
        theme (Optional[Dict], optional): _description_. Defaults to None.

    ```
    Custom Styles: 

    The dropdown UI elements can be custom styled by overriding
    the default styles supplied by the react-select callback.
    
    A custom Javascript style functions are mapped onto one or more of the keys
    listed below. React select calls the functions, passing in the
    default styles for the associated element. The custom function
    replaces the defaults as required.

    example: 

        colourStyles = {
            "control": (styles) => ({ ...styles, backgroundColor: 'white' }),

            "multiValue": (styles, { data }) => {
                const color = chroma(data.color);
                return {
                ...styles,
                backgroundColor: color.alpha(0.1).css(),
                }
            },

            "multiValueLabel": (styles, { data }) => {
                return {
                ...styles,
                color: data.color
                }
            },

            "multiValueRemove": (styles, { data }) => ({
                ...styles,
                color: data.color,
                ':hover': {
                backgroundColor: data.color,
                color: 'white',
                },
            }),
        }

        Dropdown(styles=colourStyles)

    See the following link for docs and examples. 
    
    https://react-select.com/components#adjusting-the-styling
    
        clearIndicator
        container
        control
        dropdownIndicator
        group
        groupHeading
        indicatorsContainer
        indicatorSeparator
        input
        loadingIndicator
        loadingMessage
        menu
        menuList
        menuPortal
        multiValue
        multiValueLabel
        multiValueRemove
        noOptionsMessage
        option
        placeholder
        singleValue
        valueContainer
    ```

    Returns:
        _type_: _description_
    """

    props: Dict = {"options": options}

    if close_menu_onselect is False:
        props.update({'closeMenuOnSelect': False})

    if class_name:
        props.update({'className': class_name})

    if class_name_prefix:
        props.update({'classNamePrefix': class_name_prefix})

    if default_value:
        props.update({'defaultValue': default_value})

    if id:
        props.update({'id': id})

    if multi:
        props.update({"isMulti": "true"})

    if name:
        props.update({'name': name})

    if onchange:
        props.update({"onChange": onchange})

    if styles:
        props.update({"styles": styles})

    if theme:
        props.update({"theme": theme})

    return _Select(props)
