import pytest

from playwright.sync_api import expect, Page
from tests.conftest import add_todo, get_todo_items

@pytest.mark.e2e
def test_complete_and_filter_todos(page: Page):
    add_todo(page, "Task 1")
    add_todo(page, "Task 2")

    items = get_todo_items(page)
    expect(items).to_have_count(2)

    first_item_toggle = items.nth(0).locator("input.toggle")
    first_item_toggle.check()

    counter = page.locator("footer .todo-count")
    expect(counter).to_contain_text("1 item left")

    page.locator("footer .filters >> text=Completed").click()
    completed_items = get_todo_items(page)
    expect(completed_items).to_have_count(1)
    expect(completed_items.first).to_contain_text("Task 1")

    page.locator("footer .filters >> text=Active").click()
    active_items = get_todo_items(page)
    expect(active_items).to_have_count(1)
    expect(active_items.first).to_contain_text("Task 2")
