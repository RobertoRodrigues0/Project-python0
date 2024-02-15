import pyautogui
import webbrowser
from time import sleep

def criar_publico():
    # Abra a página web
    webbrowser.open("https://adsmanager.facebook.com/adsmanager/audiences?act=1016012996344421&business_id=425651638967424&global_scope_id=425651638967424&breakdown_regrouping=1")

    # Aguarde o carregamento completo da página
    sleep(20)

    # Selecione o botão "Criar público" usando classe
    botao_criar_publico = pyautogui.locateOnScreen(".x6s0dn4 x78zum5 x1nhvcw1 x19lwn94")

    # Clique no botão
    try:
        botao_criar_publico.click()
    except:
        print("Botão 'Criar público' não encontrado.")

    # Selecione a opção "Público personalizado"
    try:
        pyautogui.click(x=105, y=197)
    except:
        print("Opção 'Público personalizado' não encontrada.")

if __name__ == "__main__":
    criar_publico()