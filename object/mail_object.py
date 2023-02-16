from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def input_username(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='username']")


def input_password(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='password']")


def submit_auth(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//input[@type='submit']")


def refresh(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//div[@class='ImgRefreshAll']")


def msg_list_1(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[4]/div[10]/div[1]/table/tbody/tr[2]/td/ul/li[1]")


def date_get(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//td[contains(@class, 'DateCol')]")


def iframe_main_body(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='zv__TV-main__MSG__body__iframe']")


def otp_selector(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/center[1]/table[1]/tbody[1]/tr[4]/td[1]/center[1]/p[1]"
    )
