import re
from time import sleep
import re
from playwright.sync_api import expect, sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    sleep(2)
    context = browser.new_context(
        color_scheme='light',
    )
    sleep(2)
    page = context.new_page(
        #base_url = 'https://selenium.dunossauro.live'
    )
    sleep(2)
    page.goto("https://selenium.dunossauro.live/todo_list.html")
    #div = page.locator('div').nth(0)#todo selecionar div 0
    # div = page.locator('id=APjFqb')#todo ID
    #div = page.locator('#APjFqb')#todo CSS
    #div = page.locator('xpath=//*[@id="#APjFqb"]')#todo XPATH
    # div = page.locator('#APjFqb > h2')#todo CSS selection

    #Mouse clique e  preenchimento de campos com texto
    sleep(1)
    page.locator('#todo-name').fill('Fazer a tarefa 01')
    sleep(1)
    page.locator('#todo-desc').fill('Descrição da  tarefa 02')
    sleep(1)
    page.locator('#todo-next').click()
    sleep(1)
    page.locator('#todo-submit').click()#todo css seletor
    sleep(1)
    page.locator('button.do').click()#todo Class seletor
    sleep(1)
    page.locator('button.do').click()
    sleep(1)
    #page.locator('class=cancel').click()
    #sleep(3)

    # Validar se preenchimento ou campo

    card = page.locator('.terminal-card')
    sleep(3)
    title = card.locator('.name')
    sleep(3)
    desc = card.locator('.description')
    sleep(3)
    #print(title.text_content(), desc.text_content())
    #expect(title).to_have_text('Fazer a tarefa 01')
    #expect(desc).to_have_text('Descrição da  tarefa 02')
    #expect(title).to_have_text(re.compile('01'))
    #     * expect 3 tipos de objeto *
    # - APIResposeAssertion

    # - LocatorAssersion
    #expect(title).not_to_have_text(re.compile('Fazer'))
    sleep(5)
    # - PageAsserton
    expect(page).to_have_title('Todo list')
    request = p.request.new_context()  # .chama o metodo
    response = request.get('https://duckduckgo.com')
    expect(response).to_be_ok()
    #breakpoint()
    browser.close()