import pytest
import reactpy
from reactpy.testing import poll

from reactpy_select.counter import ExampleCounter

# Basic test of the default custom component example.
#
#  https://github.com/reactive-python/reactpy-js-component-template/blob/main/%7B%7Bcookiecutter.repository_name%7D%7D/tests/test_example.py

@pytest.mark.anyio
async def test_example_counter(display):
    count = reactpy.Ref(0)

    await display.show(
        lambda: ExampleCounter(
            on_count_change=count.set_current,
            button_text="this is a test",
            button_id="test-button",
        )
    )

    client_side_button = await display.page.wait_for_selector("#test-button")
    poll_count = poll(lambda: count.current)

    await client_side_button.click()
    await poll_count.until_equals(1)

    await client_side_button.click()
    await poll_count.until_equals(2)
