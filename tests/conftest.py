import pytest
from playwright.sync_api import sync_playwright, Page

BASE_URL = "https://todomvc.com/examples/react/dist/"

@pytest.fixture(scope="session")
def driver():
    with sync_playwright() as p:
        dr = p.chromium.launch(headless=True)
        yield dr
        dr.close()

@pytest.fixture
def page(driver) -> Page:
    p = driver.new_page()
    p.goto(BASE_URL)

    p.evaluate("localStorage.clear()")
    p.reload()

    yield p
    p.close()

def add_todo(page: Page, text: str) -> None:
    input_box = page.locator("input.new-todo")
    input_box.fill(text)
    input_box.press("Enter")

def get_todo_items(page: Page):
    return page.locator("ul.todo-list li")
