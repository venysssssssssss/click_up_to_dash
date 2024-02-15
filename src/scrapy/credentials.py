import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login_to_clickup():
    username = 'vinicius.reis@tahto.com.br'
    password = '1a2b3c4dT!'

    try:
        # Configure o driver do navegador
        driver = webdriver.Edge()

        wait = WebDriverWait(driver, 10)

        # Acesse a página de login do Clickup
        driver.get('https://app.clickup.com/login')

        # Aguarde até que o campo de entrada de usuário/email esteja visível e interagível
        username_input = wait.until(
            EC.element_to_be_clickable((By.ID, 'login-email-input'))
        )

        # Envie o dado de login
        username_input.send_keys(username)

        # Encontre o campo de senha e insira a senha
        password_input = wait.until(
            EC.visibility_of_element_located((By.ID, 'login-password-input'))
        )
        password_input.send_keys(password)

        # Clique no botão de login
        driver.find_element(
            By.XPATH,
            '//*[@id="app-root"]/cu-login/div/div[2]/div[2]/div[1]/cu-login-form/div/form/button',
        ).click()
        time.sleep(120)
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
