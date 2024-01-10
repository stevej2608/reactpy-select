from reactpy import html, component, event, run

from reactpy_select import ExampleCounter


@component
def AppMain():
    
    @event
    def on_change(evt):
        print('Button Clicked')

    return html.div(
        html.h2('Example'),
        ExampleCounter(
            on_count_change=on_change,
            button_text="Click Me",
            button_id="test-button"
        )
    )

# python usage.py

if __name__ == "__main__":
    run(AppMain)

