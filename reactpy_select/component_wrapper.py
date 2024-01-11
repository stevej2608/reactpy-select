from typing import List, Callable, Any
from os import environ
from pathlib import Path

from reactpy.web.module import export, module_from_file

_js_module = module_from_file(
    "reactpy-select",
    file=Path(__file__).parent/"bundle.dev.js" if environ.get("REACTPY_DEBUG_MODE") else Path(__file__).parent/"bundle.min.js" ,
    fallback="⏳",
)

_Dropdown = export(_js_module, "Dropdown")

# https://react-select.com/props
# https://dash.plotly.com/dash-core-components/dropdown#examples

def Dropdown(options: List[str], onchange: Callable[[Any], None]=None, multi:bool = False):

    props = {'options' : options} 

    if multi:
         props.update({"isMulti": "true"})

    if onchange:
         props.update({"onChange": onchange})

    return _Dropdown(props)
