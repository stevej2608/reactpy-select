import reactpy
from reactpy.testing import poll

from reactpy_select.dropdown import Dropdown, ActionMeta, EventOptions

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

async def test_example_counter(display):
    options = reactpy.Ref(0)

    await display.show(
        lambda: Dropdown(options=options, id="test-dropdown")
    )

    client_side_button = await display.page.wait_for_selector("#test-dropdown")
    poll_count = poll(lambda: options.current)

    await client_side_button.click()
    await poll_count.until_equals(1)

    await client_side_button.click()
    await poll_count.until_equals(2)
