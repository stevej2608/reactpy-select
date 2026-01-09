from os import environ
from pathlib import Path

from reactpy.web.module import export, module_from_file


_js_module = module_from_file(
    "reactpy-select",
    file=Path(__file__).parent / "static" / "bundle.js",
    fallback="⏳",
)

BundleWrapper = export(_js_module, "Select")
