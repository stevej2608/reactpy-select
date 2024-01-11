from typing import Literal, Union, List, Dict, Any, Optional
from os import environ
from pathlib import Path

from reactpy.web.module import export, module_from_file

_js_module = module_from_file(
    "reactpy-select",
    file=Path(__file__).parent/"bundle.dev.js" if environ.get("REACTPY_DEBUG_MODE") else Path(__file__).parent/"bundle.min.js" ,
    fallback="⏳",
)

_ExampleCounter = export(_js_module, "ExampleCounter")

def ExampleCounter(on_count_change, button_text, button_id):
    return _ExampleCounter(
        {
            "onCountChange": on_count_change,
            "buttonText": button_text,
            "buttonId": button_id,
        }
    )
