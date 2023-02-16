from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def link_foreign_registration(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//a[@href='https://corp.tandatanganku.com/wna/registration.html']")


def link_create_account(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//a[contains(@href, 'registration')]")


def select_metode_verifikasi(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='metode_verifikasi']")


def input_kitas(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//input[@id='kitas']")


def input_passport(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='passport']")


def input_fullname(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='fullname']")


def input_place_birth(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='lbrith']")


def input_nationality(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='nationality']")


def select_gender(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='gender']")


def select_day(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='Day']")


def select_month(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='Month']")


def select_year(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='Year']")


def button_next(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[@onclick='step1()']")


def card_reg(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//div[contains(@class, 'p-3')]")


def option_onsite_face_verification_visiting(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//option[@value='ONSITE']")


def invalid_input(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//input[contains(@class, 'invalid')]")


def kitas_error(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_kitas']")


def passport_error(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_passport']")


def input_email(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='email']")


def input_handphone(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='handphone']")


def email_err(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_email']")


def phone_err(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_handphone']")


def button_next2(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[@onclick='step3()']")


def invalid_email_or_phone(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//input[contains(@class, 'is-invalid')]")


def i_have_read_radio(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[8]/form/div/div[4]/div[1]/div[7]/div/div/label/span")


def webcam(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//input[@value='Open WebCam']")


def input_img_kitas(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='imgkitas']")


def input_img_passport(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='imgpassport']")


def button_agree(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@onclick, 'cek')]")


def button_takefoto(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='takefoto']")


def button_save_data(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='ntp']")


def swal(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='swal2-content']")


def email_notif_err(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_email']")


def phone_notif_err(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_handphone']")
