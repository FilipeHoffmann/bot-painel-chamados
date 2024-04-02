from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import keyboard
import sys

class acessar_painel:
    def __init__(self,credenciais:tuple):
        self.credeciais = credenciais
        
    def sair_programa(self):
        sys.exit()
        
    def abrir_navegador(self):
        navegador = webdriver.Chrome()
        navegador.get(self.credeciais.get("url"))
        login = navegador.find_element(By.XPATH, '//*[@id="login.login"]')
        senha = navegador.find_element(By.XPATH, '//*[@id="login.senha"]')
        login.send_keys(self.credeciais.get("login"))
        senha.send_keys(self.credeciais.get("senha"))
        entrar = navegador.find_element(By.XPATH, '//*[@id="entrar"]')
        entrar.click()
        navegador.get(self.credeciais.get("url"))
        pyautogui.press("f11")
        keyboard.wait("f11")