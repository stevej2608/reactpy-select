from os import environ
from pathlib import Path

from reactpy.web.module import export, module_from_file


_js_module = module_from_file(
    "reactpy-select",
    file=Path(__file__).parent/"bundle.dev.js" if environ.get("REACTPY_DEBUG_MODE_JS") else Path(__file__).parent/"bundle.min.js" ,
    fallback="⏳",
)

BundleWrapper = export(_js_module, "Select")
