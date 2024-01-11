import reactpy
from reactpy.testing import poll

from reactpy_select.dropdown import Dropdown, ActionMeta, EventOptions

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

async def test_example_counter(display):
    count = reactpy.Ref(0)

    await display.show(
        lambda: Dropdown(options=options)
    )

    client_side_button = await display.page.wait_for_selector("#test-button")
    poll_count = poll(lambda: count.current)

    await client_side_button.click()
    await poll_count.until_equals(1)

    await client_side_button.click()
    await poll_count.until_equals(2)
