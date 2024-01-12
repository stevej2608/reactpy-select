import pytest
from reactpy import event, Ref
from reactpy.testing import DisplayFixture, poll

from reactpy_select.dropdown import Dropdown, ActionMeta, EventOptions

from .tooling.wait_stable import wait_page_stable

options: EventOptions = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

# https://playwright.dev/python/docs/next/locators
# https://playwright.dev/python/docs/next/other-locators#xpath-locator

@pytest.mark.anyio
async def test_dropdown(display: DisplayFixture):
    selected_options = Ref([])

    @event
    def onChange(newValue: EventOptions, actionMeta: ActionMeta):
        selected_options.set_current(newValue)

    await display.show(
        lambda: Dropdown(options=options, multi=True, onchange=onChange, id="dd1")
    )

    await wait_page_stable(display.page)

    poll_options = poll(lambda: selected_options.current)

    text = await display.page.locator('id=dd1').all_inner_texts()
    assert text == ['Select...']

    # Open the dropdown, select 'Strawberry' and confirm the selection

    await display.page.locator('id=dd1').click()
    await display.page.locator('text=Strawberry').click()
    await poll_options.until_equals([
        {'value': 'strawberry', 'label': 'Strawberry'}
        ])

    # Open the dropdown, select 'Vanilla' and confirm the Strawberry & Vanilla are both selected

    await display.page.locator('id=dd1').click()
    await display.page.locator('text=Vanilla').click()
    await poll_options.until_equals([
        {'value': 'strawberry', 'label': 'Strawberry'},
        {'value': 'vanilla', 'label': 'Vanilla'}
        ])

    # Remove the 'Vanilla' selection and confirm only Strawberry remains

    await display.page.get_by_label('Remove Vanilla').click()
    await poll_options.until_equals([
        {'value': 'strawberry', 'label': 'Strawberry'}
        ])

    # Click the clear button [x], and confirm selection is empty

    await display.page.locator("xpath=//*[@id=\"dd1\"]/div/div[2]/div[1]").click()
    await poll_options.until_equals([])
