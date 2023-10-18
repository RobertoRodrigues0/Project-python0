from time import sleep
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    sleep(3)
    context = browser.new_context(
        color_scheme='dark',
    )
    sleep(3)
    page = context.new_page(
        #base_url = 'https://selenium.dunossauro.live'
    )
    sleep(3)
    page.goto("https://selenium.dunossauro.live/todo_list.html")
    #

    page.locator('button.do').click()
    sleep(3)

    #breakpoint()
    browser.close()