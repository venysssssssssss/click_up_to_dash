import time

from close_pop_up import close_pop
from credentials import login_to_clickup
from get_xlsx_proj import click_entrada, click_personalizar
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Edge()
    login_to_clickup()
    time.sleep(5)
    click_entrada(driver)
    time.sleep(5)
    click_personalizar(driver)
    time.sleep(5)
    driver.quit()
