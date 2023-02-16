from selenium.webdriver.common.by import By


def h1_essential_tools_for_software(driver):
    return driver.find_element(By.XPATH, "//h1[@class='rs-h1 rs-h1_theme_dark home-page__title']")


def subtitle(driver):
    return driver.find_element(
        By.XPATH,
        "//p[@class='rs-text-1 rs-text-1_hardness_hard rs-text-1_theme_dark wt-offset-top-8']")
