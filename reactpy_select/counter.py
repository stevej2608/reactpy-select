from .bundle_wrapper import _ExampleCounter

def ExampleCounter(on_count_change, button_text, button_id):
    return _ExampleCounter(
        {
            "onCountChange": on_count_change,
            "buttonText": button_text,
            "buttonId": button_id,
        }
    )
