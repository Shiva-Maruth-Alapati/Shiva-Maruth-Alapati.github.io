import pytest
from playwright.sync_api import Page, expect

def test_blog_improvements(page: Page):
    print("Starting verification script...")
    # 1. Arrange: Go to the blog homepage.
    page.goto("http://127.0.0.1:4000/")

    # 2. Assert: Check for the new "Books" navigation link.
    books_link = page.get_by_role("link", name="Books")
    expect(books_link).to_be_visible()

    # 3. Act: Click the "Books" link.
    books_link.click()

    # 4. Assert: Check that the books page is loaded.
    expect(page).to_have_url("http://127.0.0.1:4000/books/")
    expect(page.get_by_role("heading", name="Books")).to_be_visible()

    # 5. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")
    print("Screenshot taken.")

    # 6. Act: Go back to the homepage
    page.goto("http://127.0.0.1:4000/")

    # 7. Assert: We will visually verify the theme change from the screenshot.
    print("Verification script finished.")

if __name__ == "__main__":
    pytest.main([__file__])