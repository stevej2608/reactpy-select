from typing import List, Dict, Callable, TypedDict, Literal
from .bundle import _Dropdown

# https://react-select.com/props
# https://dash.plotly.com/dash-core-components/dropdown#examples

EventOption = Dict[Literal['label', 'value'], str]

ActionTypes = Literal[
     'clear', 
     'create-option', 
     'deselect-option', 
     'pop-value', 
     'remove-value', 
     'select-option', 
     'set-value']

EventOptions = List[EventOption]

class ActionMeta(TypedDict):
    'action': ActionTypes
    'option': EventOptions | None

OnChangeEvent = Callable[[EventOptions, ActionMeta], None]

def Dropdown(options: List[str], onchange: OnChangeEvent=None, multi:bool = False):

    props = {'options' : options} 

    if multi:
         props.update({"isMulti": "true"})

    if onchange:
         props.update({"onChange": onchange})

    return _Dropdown(props)
