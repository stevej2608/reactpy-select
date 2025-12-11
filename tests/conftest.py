import pytest
from playwright.async_api import async_playwright
from reactpy.testing import BackendFixture, DisplayFixture


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--headed",
        dest="headed",
        action="store_true",
        help="Open a browser window when running web-based tests",
    )


@pytest.fixture(scope="session")
async def display(backend, browser):
    async with DisplayFixture(backend, browser) as display_fixture:
        display_fixture.page.set_default_timeout(10000)
        yield display_fixture


@pytest.fixture(scope="session")
async def backend():
    async with BackendFixture() as backend_fixture:
        yield backend_fixture


@pytest.fixture(scope="session")
async def browser(pytestconfig: pytest.Config):
    async with async_playwright() as pw:
        yield await pw.chromium.launch(headless=not bool(pytestconfig.option.headed))
