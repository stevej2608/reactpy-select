from reactpy import component
from reactpy.testing import DisplayFixture
from reactpy_select import Select, Options

from .tooling.wait_stable import wait_page_stable

options: Options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

async def test_placeholder(display: DisplayFixture):
    
    @component
    def App():
        return Select(options=options, placeholder="Type Something...",id="dd1")
    
    await display.show(App)
    await wait_page_stable(display.page)

    text = await display.page.locator('id=dd1').all_inner_texts()
    assert text == ['Type Something...']
