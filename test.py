from datetime import datetime

from conftest import url, robot, delay

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
wna = form_wna_object
mail = mail_object
url_mail = url["mail-testing"]
url_staging = url["test"]


def test_crp1_1(driver):
    wna.link_create_account(driver).click()
    wna.link_foreign_registration(driver).click()

    try:
        assert wna.card_reg(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_2(driver, **kwargs):
    not_filled = kwargs.get("not_filled", "kitas")
    is_same = kwargs.get("is_same", False)
    registered = kwargs.get("registered", [False, ''])
    num_kitas = kwargs.get("kitas", "123456789")
    is_next = kwargs.get("is_next", True)

    test_crp1_1(driver)

    text_method = wna.option_onsite_face_verification_visiting(driver).text
    Select(wna.select_metode_verifikasi(driver)).select_by_visible_text(text_method)

    if not_filled is "kitas":
        wna.input_passport(driver).send_keys("123456789")
        if is_same:
            wna.input_kitas(driver).send_keys(num_kitas)
            for i in range(8):
                wna.input_kitas(driver).send_keys(Keys.BACKSPACE)
                delay(1)
            wna.input_kitas(driver).send_keys("23456789")
        robot.press("ctrl")
        robot.press("alt")
    else:
        wna.input_kitas(driver).send_keys(num_kitas)
        if is_same:
            wna.input_passport(driver).send_keys("123456789")
            for i in range(8):
                wna.input_passport(driver).send_keys(Keys.BACKSPACE)
                delay(1)
            wna.input_passport(driver).send_keys("23456789")
        robot.press("ctrl")
        robot.press("alt")

    if registered[0] is True:
        if registered[1] is "kitas":
            wna.input_kitas(driver).clear()
            wna.input_kitas(driver).send_keys("1")
            wna.input_passport(driver).send_keys("23456789")
        elif registered[1] is "passport":
            wna.input_passport(driver).clear()
            wna.input_passport(driver).send_keys("12")
            wna.input_kitas(driver).send_keys("23456789")
    else:
        pass

    robot.press("ctrl")
    robot.press("alt")
    delay(10)

    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")

    delay(10)

    if is_next:
        wna.button_next(driver).click()

    if is_same is True or registered[0] is True:
        try:
            assert wna.kitas_error(driver) is not None
            print("passed")
        except AssertionError as e:
            raise e
    else:
        try:
            assert wna.invalid_input(driver) is not None
            print("passed")
        except AssertionError as e:
            raise e


def test_crp1_3(driver):
    test_crp1_2(driver, not_filled="passport")


def test_crp1_4(driver):
    test_crp1_2(driver, is_same=True, not_filled="kitas", registered=[True, ''], is_next=False)


def test_crp1_5(driver):
    test_crp1_2(driver, is_same=False, not_filled="passport", registered=[True, "kitas"], is_next=False)


def test_crp1_6(driver):
    test_crp1_2(driver, is_same=False, not_filled="kitas", registered=[True, "passport"], is_next=False)


def test_crp1_7(driver):
    test_crp1_3(driver)

    wna.input_passport(driver).send_keys("89239834")
    wna.input_passport(driver).send_keys(Keys.ENTER)
    wna.input_nationality(driver).clear()
    wna.input_nationality(driver).send_keys(Keys.ENTER)
    wna.button_next(driver).click()
    delay(2)

    try:
        assert wna.invalid_input(driver) is not None
        print("passed")
    except AssertionError as e:
        raise e


def test_crp1_8(driver):
    test_crp1_2(driver, is_same=True, not_filled="kitas", registered=[True, ""])

    delay(3)

    try:
        assert wna.invalid_input(driver) is not None
        assert wna.input_kitas(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_9(driver):
    test_crp1_1(driver)

    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_passport(driver).send_keys("123456789")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")
    wna.button_next(driver).click()

    delay(10)

    wna.input_kitas(driver).send_keys("87723839")
    wna.input_passport(driver).clear()
    wna.input_passport(driver).send_keys(Keys.ENTER)

    wna.button_next(driver).click()
    delay(10)
    robot.press('ctrl')
    robot.press('alt')

    try:
        assert wna.passport_error(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_10(driver, **kwargs):
    num = kwargs.get("num", "0987654321")
    em_num = kwargs.get("em_num_err", "email")
    used = kwargs.get("used", False)
    test_crp1_1(driver)

    wna.input_kitas(driver).send_keys("87723839")
    wna.input_passport(driver).send_keys("123456789")
    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")
    delay(2)
    wna.button_next(driver).click()

    if used is False:
        if em_num is "email":
            wna.input_email(driver).send_keys("tandatangan")

            delay(4)

            try:
                assert wna.email_err(driver) is not None
            except AssertionError as e:
                raise e
        elif em_num is "phone":
            wna.input_handphone(driver).send_keys(num)

            delay(4)

            try:
                assert wna.phone_err(driver) is not None
            except AssertionError as e:
                raise e


def test_crp1_11(driver):
    test_crp1_1(driver)

    wna.input_kitas(driver).send_keys("87723839")
    wna.input_passport(driver).send_keys("123456789")
    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")
    delay(2)
    wna.button_next(driver).click()

    wna.input_email(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
    wna.input_handphone(driver).send_keys("89992738367")
    robot.press('ctrl')

    delay(4)

    try:
        assert wna.email_notif_err(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_12(driver):
    test_crp1_1(driver)

    wna.input_kitas(driver).send_keys("87723839")
    wna.input_passport(driver).send_keys("123456789")
    wna.input_fullname(driver).send_keys("John Doe")
    wna.input_place_birth(driver).send_keys("Bangkok")
    wna.input_nationality(driver).send_keys("Thailand")
    Select(wna.select_year(driver)).select_by_visible_text("1993")
    delay(2)
    wna.button_next(driver).click()

    wna.input_email(driver).send_keys("dstest4@tandatanganku.com")
    wna.input_handphone(driver).send_keys("87804070516" + Keys.ENTER)
    robot.press('ctrl')

    delay(4)

    try:
        assert wna.phone_notif_err(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_13(driver):
    test_crp1_10(driver, num="23", em_num_err="phone")


def test_crp1_14(driver):
    test_crp1_10(driver, num="897", em_num_err="phone")


def test_crp1_15(driver):
    test_crp1_10(driver, used=True)

    wna.input_email(driver).send_keys("dstest4@tandatanganku.com")
    wna.button_next2(driver).click()
    delay(2)

    try:
        assert wna.invalid_email_or_phone(driver) is not None
    except AssertionError as e:
        raise e


def test_crp1_16(driver, **kwargs):
    """its semi-automation because its input a captcha"""
    up_photo = kwargs.get("up_photo", "passport")
    test_crp1_10(driver, used=True)

    wna.input_handphone(driver).send_keys("89977882983")
    wna.input_email(driver).send_keys("dstest4@tandatanganku.com")

    delay(2)
    wna.button_next2(driver).click()

    if up_photo is "passport":
        wna.input_img_passport(driver).send_keys("D:\\local\\automationTest\\file\\image.jpeg")
    elif up_photo is "kitas":
        wna.input_img_kitas(driver).send_keys("D:\\local\\automationTest\\file\\image.jpeg")

    wna.webcam(driver).click()
    delay(10)
    wna.button_takefoto(driver).click()

    wna.i_have_read_radio(driver).click()
    delay(5)
    wna.button_agree(driver).click()

    delay(17)
    wna.button_save_data(driver).click()

    delay(3)


def test_crp1_17(driver):
    """its semi-automation because its input a captcha"""
    test_crp1_16(driver, up_photo="kitas")


def test_crp1_18(driver):
    """its semi-automation because its input a captcha"""
    test_crp1_10(driver, used=True)

    wna.input_handphone(driver).send_keys("89977882983")
    wna.input_email(driver).send_keys("dstest4@tandatanganku.com")

    delay(2)
    wna.button_next2(driver).click()

    wna.input_img_passport(driver).send_keys("D:\\local\\automationTest\\file\\image.jpeg")
    wna.input_img_kitas(driver).send_keys("D:\\local\\automationTest\\file\\image.jpeg")

    wna.i_have_read_radio(driver).click()
    delay(5)
    wna.button_agree(driver).click()

    delay(17)
    wna.button_save_data(driver).click()

    delay(5)


def test_crp1_19(driver):
    test_crp1_10(driver, used=True)

    wna.input_handphone(driver).send_keys("89977882983")
    wna.input_email(driver).send_keys("dstest4@tandatanganku.com")

    delay(2)
    wna.button_next2(driver).click()

    wna.input_img_passport(driver).send_keys("D:\\local\\automationTest\\file\\image.jpeg")
    wna.input_img_kitas(driver).send_keys("D:\\local\\automationTest\\file\\image.jpeg")

    wna.webcam(driver).click()
    delay(10)
    wna.button_takefoto(driver).click()

    wna.i_have_read_radio(driver).click()
    delay(5)
    wna.button_agree(driver).click()

    delay(17)

    wna.button_save_data(driver).click()

    delay(3)


# def test_crp1_20(driver):

def test_crp1_21(driver):
    test_crp1_10(driver, used=True)

    wna.input_handphone(driver).send_keys("89977882983")
    wna.input_email(driver).send_keys("dstest4@tandatanganku.com")

    delay(2)
    wna.button_next2(driver).click()

    wna.input_img_passport(driver).send_keys("file/image.jpeg")
    wna.input_img_kitas(driver).send_keys("file/image.jpeg")

    wna.webcam(driver).click()
    delay(10)
    wna.button_takefoto(driver).click()

    wna.i_have_read_radio(driver).click()
    delay(5)
    wna.button_agree(driver).click()

    delay(17)

    wna.button_save_data(driver).click()

    delay(3)


def test_crp1_22(driver):
    test_crp1_21(driver)
    time_test = datetime.now()

    driver.execute_script("window.open('about:blank','tab2')")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url_mail)

    mail.input_username(driver).send_keys("dstest4@tandatanganku.com")
    mail.input_password(driver).send_keys("dstest123" + Keys.ENTER)
    delay(5)

    for i in range(5):
        mail.refresh(driver).click()
        delay(1)

    ActionChains(driver).double_click(mail.msg_list_1(driver)).perform()

    date_received = mail.date_get(driver).text
    cvrt_date_received = datetime.strptime(date_received, "%B %d, %Y %I:%M %p")

    try:
        if cvrt_date_received <= time_test:
            print("\nTime WNA Registration is below than email received")
        else:
            raise Exception("\nThe message date is not more than now")
    except Exception as e:
        print(e)

    delay(2)
