from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def filter_action(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//select[@name='status']")


def filter_submit(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]")


def choose_account(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div/div/div/div/section/form/a[1]/div")


def check_seal_doc(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[.//*[@id='ckseal']]")


def nav_inbox(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//li[.//i[@class='ti-write']]")


def kotak_masuk(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[2]/ul/li[3]/a")


def name_first_receiver(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='name-1']")


def btn_detail_doc(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='detail_doc']")


def btn_add_sign(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[@onclick='adds_ttd()']")


def sign_zone_1(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//div[@class='foo blue ui-resizable']")


def lock_sign_1(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='lock1']")


def lock_paraf_1(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='lockinit1']")


def resizing_zone_1(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//div[contains(@class, 'ui-icon')]")


def btn_set_email(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[16]/div/div/div/div/div/div[3]/button")


def btn_process_send_doc(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='pros']")


def btn_send_doc(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='send']")


def need_sign(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//a[contains(@href, 'needsign')]")


def check_all_sign(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='idbox']")


def sign_all_btn(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[@id='signnow']")


def email_first_receiver(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='email-1']")


def proses_btn(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@class, 'swal2-confirm')]")


def check_doc1(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='checkbox1']")


def check_doc2(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='checkbox2']")


def check_doc3(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='checkbox3']")


def check_doc4(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='checkbox4']")


def otp_input_number(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='otp']")


def otp_email(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='otemail']")


def proses_doc_btn_submit(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='ps12']")


def yakin_btn(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@class, 'swal2-confirm')]")


def link_tooltip1(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[2]/div[3]/div/span")


def btn_selesai(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//a[@class='btn btn-info']")


def button_proses_sign_one(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[@onclick='proOtp()']")


def modal_title_process(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[15]/div/div/div[1]/h4")


def label_iya(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='p1']")


def label_tidak(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='p2']")


def text_area_reason(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='reason']")


def btn_otp_sms(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='btnotp']")


def btn_otp_email(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='otemail']")


def btn_prosign(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='prosign']")


def title_verify_false(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[text() = 'Kode verifikasi salah']")


def btn_saya_yakin(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@class, 'confirm')]")


def verify_false(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[text() = 'Kode verifikasi salah']")


def btn_swal_ok(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@class, 'swal-button')]")


def btn_tidak_yakin(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@class, 'swal-button--cancel')]")


def title_proses_dibatalkan(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[text() = 'Proses dibatalkan']")


def title_modal_proses(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[15]/div/div/div[1]/h4")


def btn_gagal_otp(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='bModal']")


def button_add_me(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='add_me']")


def select_action_need(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//select[@id='ck1']")


def select_action_need_2(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//select[@id='ck2']")


def button_add_receiver(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='add_re']")


def input_name_receiver_2(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='name-2']")


def input_email_receiver_2(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='email-2']")


def canvas(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='pdf-canvas']")


def label_sort_sign(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//label[@for='seq1']")


def btn_choose_expired_date(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//i[@role='right-icon']")


def btn_previous_month_date(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//i[@class='gj-icon chevron-left']")


def date(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/div")


def button_ok_date(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[2]")


def icon_x_swal(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//span[@class='swal2-x-mark']")


def button_swal_confirm_ok(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@class, 'swal2-confirm')]")


def err_email_receiver(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_email-1']")


def err_email_receiver_2(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_email-2']")


def err_name_receiver(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='e_name-1']")


def button_paraf(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@onclick, 'adds_init()')]")


def paraf_box(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='imginit-1']")


def confirm_after_send_doc(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//button[contains(@style, '133,')]")


def link_home(driver) -> WebElement:
    return driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[1]/a")


def dropdown_dokumen(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "//a[contains(@href, 'javascript:void(0)')][.//i[@class='ti-write']]")


def link_draf(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[2]/ul/li[1]/a")


def btn_send_row_one_file_draf(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[3]/btn[3]")


def btn_hapus_file_draf(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[3]/btn[1]")


def btn_lihat_file_draf(driver) -> WebElement:
    return driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[3]/btn[2]")


def sign_null(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='swal2-content']")


def select_email_seal(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//select[@id='seal']")


def imgsealer(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='imgsealer']")


def button_lockseal(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//*[@id='lockseal']")


def kotak_masuk_terakhir(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//div[@data-target='#demo1']")


def tanggal_kotak_masuk(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[2]/div[3]/div")


def latest_tandatangan(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[2]/div[3]/div/span"
    )


def link_terkirim(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[1]/div[2]/div[3]/div[1]/nav/ul/li[2]/ul/li[2]/a")


def btn_eye(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[12]/div/div/div/div/div/div/div[2]/div[4]/ul/li[2]/a/i")


def swal_otp_none(driver) -> WebElement:
    return driver.find_element(By.XPATH, "//div[contains(@class, 'swal-text')]")


def second_tandatangan(driver) -> WebElement:
    return driver.find_element \
        (By.XPATH,
         "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[4]/div[3]/div/span")


def third_tandatangan(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[6]/div[3]/div/span")


def fourth_tandatangan(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[11]/div[6]/div/div/div[1]/div/div/div/div[10]/div[3]/div/span")


def latest_inbox(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/div/div[2]/div[3]/div/span")


def latest_inbox2(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/div/div[4]/div[3]/div/span")


def latest_inbox3(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/div/div[6]/div[3]/div/span")


def latest_inbox4(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/div/div[8]/div[3]/div/span")


def latest_inbox5(driver) -> WebElement:
    return driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div[2]/div[2]/div[12]/div/div[3]/div/div/div/div[10]/div[3]/div/span")
