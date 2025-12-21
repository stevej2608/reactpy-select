from typing import Any, Dict, List, Literal, Optional, TypedDict

from reactpy.types import EventHandlerType, VdomDict

from .bundle_wrapper import BundleWrapper

# https://react-select.com/props
# https://dash.plotly.com/dash-core-components/dropdown#examples


Option = Dict[str, Any]

Options = List[Option]

ActionTypes = Literal[
    "clear",
    "create-option",
    "deselect-option",
    "pop-value",
    "remove-value",
    "select-option",
    "set-value",
]


class ActionMeta(TypedDict):
    action: ActionTypes
    option: Optional[Options]

# Theme customization, see:
#   https://react-select.com/styles#overriding-the-theme
#   https://github.com/JedWatson/react-select/blob/master/packages/react-select/src/theme.ts
#

def Select(
    options: Optional[Options] = None,
    close_menu_onselect: Optional[bool] = True,
    class_name: Optional[str] = None,
    class_name_prefix: Optional[str] = None,
    default_value: Optional[Options] = None,
    id: Optional[str] = None,
    is_clearable: Optional[bool] = None,
    is_disabled: Optional[bool] = None,
    is_loading: Optional[bool] = None,
    is_searchable: Optional[bool] = None,
    multi: bool = False,
    name: Optional[str] = None,
    onchange: Optional[EventHandlerType] = None,
    placeholder: Optional[str] = None,
    styles:  Optional[Dict[str, Any]] = None,
    theme:  Optional[Dict[str, Any]] = None,
    value: Optional[Options] = None,
    ) -> VdomDict:
    """ReactPy wrapper for react-select component

    Args:
        options (Options): _description_
        close_menu_onselect (Optional[bool], optional): _description_. Defaults to True.
        class_name (Optional[str], optional): _description_. Defaults to None.
        class_name_prefix (Optional[str], optional): _description_. Defaults to None.
        default_value (Options, optional): _description_. Defaults to None.
        id (Optional[str], optional): _description_. Defaults to None.
        is_clearable (Optional[bool], optional): _description_. Defaults to None.
        is_disabled (Optional[bool], optional): _description_. Defaults to None.
        is_loading (Optional[bool], optional): _description_. Defaults to None.
        is_searchable (Optional[bool], optional): _description_. Defaults to None.
        multi (bool, optional): _description_. Defaults to False.
        name (Optional[str], optional): _description_. Defaults to None.
        onchange (Optional[OnChangeEvent], optional): _description_. Defaults to None.
        placeholder (Optional[str], optional): _description_. Defaults to None.
        styles (Optional[Dict], optional): _description_. Defaults to None.
        theme (Optional[Dict], optional): _description_. Defaults to None.
        value (Options, optional): _description_. Defaults to None.

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

    props: Dict[str, Any] = {"options": options}

    if close_menu_onselect is False:
        props.update({'closeMenuOnSelect': False})

    if class_name:
        props.update({'className': class_name})

    if class_name_prefix:
        props.update({'classNamePrefix': class_name_prefix})

    if default_value:
        props.update({'defaultValue': default_value})

    if is_clearable is not None:
        props.update({'isClearable': is_clearable})

    if is_disabled is not None:
        props.update({'isDisabled': is_disabled})

    if is_loading is not None:
        props.update({'isLoading': is_loading})

    if is_searchable is not None:
        props.update({'isSearchable': is_searchable})

    if id:
        props.update({'id': id})

    if multi:
        props.update({"isMulti": "true"})

    if name:
        props.update({'name': name})

    if onchange:
        from reactpy import event as reactpy_event
        import inspect

        # Wrap the event handler to convert dict with numeric keys back to list
        @reactpy_event
        async def wrapped_handler(newValue: Any, actionMeta: Any) -> Any:
            # ReactPy 2.0 serializes JS arrays as dicts with numeric string keys
            if isinstance(newValue, dict):
                if not newValue:
                    # Empty dict means empty array
                    newValue = []
                elif all(str(k).isdigit() for k in newValue.keys()):  # type: ignore
                    # Convert dict with numeric keys to list
                    newValue = [newValue[str(i)] for i in range(len(newValue))]  # type: ignore

            # Get the underlying function from EventHandler if needed
            handler_func = onchange.function if hasattr(onchange, 'function') else onchange  # type: ignore
            # Pass as a tuple since the underlying wrapper expects unpacked args
            result = handler_func((newValue, actionMeta))  # type: ignore
            # Await if it's a coroutine
            if inspect.iscoroutine(result):  # type: ignore
                return await result  # type: ignore
            return result  # type: ignore

        props.update({"onChange": wrapped_handler})

    if placeholder:
        props.update({"placeholder": placeholder})

    if styles:
        props.update({"styles": styles})

    if theme:
        props.update({"theme": theme})

    if value:
        props.update({'value': value})

    return BundleWrapper(props)
