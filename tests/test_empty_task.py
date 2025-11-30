import pytest

from playwright.sync_api import expect, Page
from tests.conftest import get_todo_items

@pytest.mark.e2e
def test_empty_todo_is_not_created(page: Page):
    items = get_todo_items(page)
    initial_count = items.count()

    input_box = page.locator("input.new-todo")
    input_box.press("Enter")

    final_count = items.count()
    assert final_count == initial_count
