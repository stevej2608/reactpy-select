from os import environ
from pathlib import Path

from reactpy.web.module import export, module_from_file

from utils.logger import log

log.warning('REACTPY_DEBUG_MODE=%s', environ.get("REACTPY_DEBUG_MODE"))

_js_module = module_from_file(
    "reactpy-select",
    file=Path(__file__).parent/"bundle.dev.js" if environ.get("REACTPY_DEBUG_MODE") else Path(__file__).parent/"bundle.min.js" ,
    fallback="⏳",
)

_Dropdown, _ExampleCounter = export(_js_module, ["Dropdown", "ExampleCounter"])
