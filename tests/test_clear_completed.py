import pytest

from playwright.sync_api import expect, Page
from tests.conftest import add_todo, get_todo_items

@pytest.mark.e2e
def test_clear_completed_removes_only_done_tasks(page: Page):
    add_todo(page, "Done task")
    add_todo(page, "Active task")

    items = get_todo_items(page)
    expect(items).to_have_count(2)

    done_item = items.nth(0)
    done_item.locator("input.toggle").check()

    classes = done_item.get_attribute("class") or ""
    assert "completed" in classes

    page.locator("text=Clear completed").click()

    remaining = get_todo_items(page)
    expect(remaining).to_have_count(1)
    expect(remaining.first).to_contain_text("Active task")
