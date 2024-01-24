import pytest
from reactpy.testing import DisplayFixture
from reactpy_select import Select, Options

from .tooling.wait_stable import wait_page_stable

options: Options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

@pytest.mark.anyio
async def test_placeholder(display: DisplayFixture):

    await display.show(
        lambda: Select(options=options, placeholder="Type Something...",id="dd1")
    )

    await wait_page_stable(display.page)

    text = await display.page.locator('id=dd1').all_inner_texts()
    assert text == ['Type Something...']
