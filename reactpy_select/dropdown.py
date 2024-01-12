from typing import List, Dict, Callable, TypedDict, Literal, Optional
from .bundle_wrapper import _Dropdown

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

# https://codesandbox.io/p/sandbox/codesandboxer-example-rx8xjs?file=%2Fexample.tsx%3A8%2C5-8%2C56

def Dropdown(
    options: Options,
    class_name: Optional[str] = None,
    class_name_prefix: Optional[str] = None,
    default_value: Options = None,
    id: Optional[str] = None,
    multi: bool = False,
    name: Optional[str] = None,
    onchange: Optional[OnChangeEvent] = None,
    ):

    props: Dict = {"options": options}

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

    return _Dropdown(props)
