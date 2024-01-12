import pytest
from reactpy.testing import DisplayFixture
from examples.simple import AppMain

from .tooling.wait_stable import wait_page_stable

options = [
  { 'value': 'chocolate', 'label': 'Chocolate' },
  { 'value': 'strawberry', 'label': 'Strawberry' },
  { 'value': 'vanilla', 'label': 'Vanilla' }
]

# https://playwright.dev/python/docs/next/locators

@pytest.mark.anyio
async def test_example_dropdown(display: DisplayFixture):
    await display.show(AppMain)
    await wait_page_stable(display.page)

    # Unselected state

    text = await display.page.locator('id=dd1').all_inner_texts()
    assert text == ['Select...']

    # Dropdown state, verify all options are listed in the dropdown

    await display.page.locator('id=dd1').click()
    text = await display.page.locator('role=listbox').all_inner_texts()
    assert text == ['Chocolate\nStrawberry\nVanilla']

    # Select an option from the dropdown and confirm the selection

    await display.page.locator('text=Strawberry').click()
    text = await display.page.locator('id=dd1').all_inner_texts()
    assert text == ['option Strawberry, selected.\nStrawberry']
