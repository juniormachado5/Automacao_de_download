import pyautogui
import webbrowser
from time import sleep

def site_automacao():
    #Abrir o site
    webbrowser.open('https://cursoautomacao.netlify.app/')
    sleep(2)

    #encontrar o campo
    pyautogui.moveTo(2816,179, duration=2)
    pyautogui.scroll(-600)
    sleep(1)

    #clicar  e digitar o nome 
    pyautogui.moveTo(3399,372, duration=2)
    pyautogui.click()
    pyautogui.typewrite('junior machado')


    # criar o alerta 
    pyautogui.click(3393,409, duration=2)
    pyautogui.click(3053,161, duration=2)
    sleep(1)

    # subir toda a página 
    pyautogui.moveTo(2880,219, duration=2)
    pyautogui.scroll(600)
    sleep(1)

    #rolar ate o dowloads 
    pyautogui.moveTo(2880,219, duration=2)
    pyautogui.scroll(-1200)

    #fazer o dowload
    pyautogui.click(2393,510, duration=2)
    pyautogui.click(2392,47, duration=2)
    pyautogui.click(2589,513, duration=2)

#avisando e criando alerta de terminou
site_automacao()
pyautogui.alert(text="Você Terminou", title='Automação Site', button='ok')

