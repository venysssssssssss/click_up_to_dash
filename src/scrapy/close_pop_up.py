import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def close_pop(driver):
    try:
        # Espera até que o elemento de pop-up esteja presente na página
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app-root"]/cu-modal-keeper/cu-modal/div/div[2]/div[2]/div[2]/cu-clickup-3-switcher/div',
                )
            )
        )

        # Clique para fechar o elemento
        driver.find_element(By.XPATH, '//*[@id="app-root"]/cu-modal-keeper/cu-modal/div/div[2]/div[2]/div[1]/div/button').click()

        print('Pop-up fechado com sucesso.')

    except Exception as e:
        print(f'Erro ao fechar o pop-up: {e}')
