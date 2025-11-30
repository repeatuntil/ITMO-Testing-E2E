import pytest

from playwright.sync_api import expect, Page
from tests.conftest import add_todo, get_todo_items

@pytest.mark.e2e
def test_add_single_todo_appears_in_list(page: Page):
    add_todo(page, "Сделать лабораторную")

    items = get_todo_items(page)
    expect(items).to_have_count(1)
    expect(items.first).to_contain_text("Сделать лабораторную")

    counter = page.locator("footer .todo-count")
    expect(counter).to_contain_text("1 item left")
