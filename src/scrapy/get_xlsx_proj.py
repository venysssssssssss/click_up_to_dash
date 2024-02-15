from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def click_entrada(driver):
    try:
        wait = WebDriverWait(driver, 10)
        entrada_button = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/cu-simple-bar/div[1]/div[3]/cu-sidebar-favorites/button'))
        )
        entrada_button.click()
    except Exception as e:
        print(f"Erro ao clicar no elemento 'Entrada': {e}")

def click_personalizar(driver):
    try:
        wait = WebDriverWait(driver, 10)
        personalizar_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/main/cu-dashboard/div/cu-views-bar-container/cu2-views-bar/div[1]/div[1]/div/button[2]'))
        )
        personalizar_button.click()
    except Exception as e:
        print(f"Erro ao clicar no elemento 'Personalizar': {e}")