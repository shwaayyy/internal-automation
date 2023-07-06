from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import url, delay, robot

from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
mail = mail_object
url_mail = url["mail-testing"]
url_staging = url["app"]


def test_reg_page(driver):
    form.link_reg(driver).click()
    delay(3)


def test_reg_nik(driver):
    form.link_reg(driver).click()
    delay(0.5)
    form.nik_input(driver).send_keys("8928839489849203")
    delay(3)


def test_format16_nik(driver):
    test_reg_page(driver)

    form.nik_input(driver).send_keys("920390239239")
    delay(0.5)
    assert form.error_format16_nik(driver) is not None
    delay(2)


def test_format_false(driver):
    test_reg_page(driver)

    form.nik_input(driver).send_keys("0")
    delay(0.5)
    assert form.error_format_false(driver) is not None
    delay(2)


def test_cant_input_string(driver):
    test_reg_page(driver)

    form.nik_input(driver).send_keys("a")
    delay(0.5)

    assert form.error_format16_nik(driver) is not None


def test_nik_registered(driver):
    test_reg_page(driver)

    form.nik_input(driver).send_keys("3275025302090003")
    delay(0.5)
    form.birth_place_input(driver).send_keys("jakarta")
    form.btn_next_step1(driver).click()

    assert form.validation_name(driver) is not None


def test_birth_place_validation(driver, **kwargs):
    is_use = kwargs.get("use", False)
    test_reg_page(driver)

    form.nik_input(driver).send_keys("3275025302090003")
    delay(0.5)
    form.name_input(driver).send_keys("mimio")

    Select(form.gender_select(driver)).select_by_visible_text("Perempuan")
    delay(5)

    if is_use:
        form.birth_place_input(driver).send_keys("jakarta")
        delay(5)
        form.btn_next_step1(driver).click()
    else:
        form.btn_next_step1(driver).click()
        delay(5)
        assert form.validation_place(driver) is not None


def test_full_identity(driver):
    test_birth_place_validation(driver, use=True)
    delay(3)

    assert form.step2(driver) is not None


def test_empty_username(driver):
    test_birth_place_validation(driver, use=True)

    form.password_reg(driver).send_keys("asdf1234!")
    form.password_confirmation(driver).send_keys("asdf1234!")

    form.email_input_register(driver).send_keys("testing223@spambox.xyz")
    form.phone_input_register(driver).send_keys("89237738883")

    form.step3(driver).click()
    delay(3)
    assert form.validation_username(driver) is not None


def test_minus_characters_username(driver):
    test_birth_place_validation(driver, use=True)
    form.username(driver).send_keys("asd")
    delay(1)

    assert form.err_username(driver) is not None
    delay(1.5)


def test_username_registered(driver):
    test_birth_place_validation(driver, use=True)

    form.username(driver).send_keys("wahyuhidy")
    delay(1)

    assert form.username_registered(driver) is not None
    delay(1.5)


def test_password_too_short(driver):
    test_birth_place_validation(driver, use=True)

    form.password_reg(driver).send_keys("hi!23")
    delay(3)
    assert form.password_too_short(driver) is not None
    delay(1)


def test_minus_symbol_pass(driver):
    test_birth_place_validation(driver, use=True)

    form.password_reg(driver).send_keys("asda")
    delay(2)
    assert form.password_minus_symbol(driver) is not None


def test_strong_password(driver):
    test_birth_place_validation(driver, use=True)

    form.password_reg(driver).send_keys("Mamang123!")
    delay(2)

    assert form.strong_password(driver) is not None


def test_password_is_not_same(driver):
    test_birth_place_validation(driver, use=True)

    form.password_reg(driver).send_keys("Mamang123!")
    form.password_confirmation(driver).send_keys("Mam2131")

    delay(2)

    assert form.pass_not_same(driver) is not None


def test_email_validation(driver):
    test_birth_place_validation(driver, use=True)

    form.username(driver).send_keys("kijang")
    form.password_reg(driver).send_keys("Mamang123!")
    form.password_confirmation(driver).send_keys("Mam2131")
    form.phone_input_register(driver).send_keys("89773827839")

    form.step3(driver).click()
    delay(2)

    assert form.validation_email(driver) is not None


def test_email_taken(driver, **kwargs):
    email = kwargs.get("email", "ditest10@tandatanganku.com")
    test_obj = kwargs.get("obj", "email_taken")
    test_birth_place_validation(driver, use=True)
    delay(2)
    form.email_input_register(driver).send_keys(email)
    delay(3)

    if test_obj is "email_taken":
        assert form.email_taken(driver) is not None
    elif test_obj is "email_invalid":
        assert form.email_invalid(driver) is not None
    else:
        pass


def test_invalid_email(driver):
    test_email_taken(driver, obj="email_invalid", email="asdas")


def test_invalid_number(driver):
    test_birth_place_validation(driver, use=True)

    form.step3(driver).click()
    delay(2)
    assert form.number_invalid(driver) is not None


def test_number_taken(driver):
    test_birth_place_validation(driver, use=True)

    form.phone_input_register(driver).send_keys("87804070516")
    delay(4)

    is_display = form.number_taken(driver).is_displayed()

    print(f"\nnumber taken is: {is_display}")

    assert form.number_taken(driver) is not None


def test_false_format_number(driver):
    test_birth_place_validation(driver, use=True)

    form.phone_input_register(driver).send_keys("09123")
    delay(1)
    assert form.false_number_format(driver) is not None


def test_number_less_than_8(driver):
    test_birth_place_validation(driver, use=True)

    form.phone_input_register(driver).send_keys("892")
    delay(1)

    assert form.number_less_than_8(driver) is not None


def test_true_identity(driver, **kwargs):
    inherit = kwargs.get("inherit", False)
    test_birth_place_validation(driver, use=True)

    form.username(driver).send_keys("asdteuse782")
    delay(2)
    form.password_reg(driver).send_keys("Mamang123!")
    form.password_confirmation(driver).send_keys("Mamang123!")
    form.email_input_register(driver).send_keys("amang78@spambox.xyz")
    form.phone_input_register(driver).send_keys("89099277272" + Keys.ENTER)
    robot.press("enter")

    delay(5)

    for i in range(10):
        form.step3(driver).click()
        delay(2)
        ActionChains(driver).double_click(form.step3(driver)).perform()
        if form.step3_title(driver) is not None:
            break

    if inherit:
        pass
    else:
        assert form.step3_title(driver) is not None

    delay(10)


def test_input_ktp(driver):
    test_true_identity(driver, inherit=True)

    delay(2)
    form.span_ktp_input(driver).click()
    delay(4)

    robot.press("escape")
    delay(2)
    form.ktp_input(driver).send_keys("C:\\wahyu\\dummy file\\ktp aziz.jpg")
    delay(5)


def test_input_selfie(driver):
    test_true_identity(driver, inherit=True)

    form.button_webcam(driver).click()
    delay(4)
    form.button_selfie_submit(driver).click()

    delay(5)


def test_draw_signature(driver):
    test_true_identity(driver, inherit=True)

    form.button_draw_sign(driver).click()

    delay(10)

    form.button_save_ttd(driver).click()
    delay(2)


def test_input_captcha(driver):
    test_true_identity(driver, inherit=True)



