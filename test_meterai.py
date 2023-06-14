from typing import Union
from conftest import url, delay

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
mail = mail_object
url_mail = url["mail-testing"]
url_staging = url["test"]


def test_emet_login(driver, **kwargs):
    """test login"""
    seal = kwargs.get('seal', False)

    if seal is False:
        form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
        delay(2)
        form.password(driver).send_keys("Coba1234" + Keys.ENTER)
        delay(4)
    else:
        form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
        delay(2)
        form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
        delay(4)
        doc.choose_account(driver).click()

    delay(3)


def test_doc_upload(driver, **kwargs):
    """Unggah Dokumen PDF"""
    is_seal = kwargs.get('seal', False)
    is_pdf = kwargs.get('exe', 'pdf')

    test_emet_login(driver, seal=is_seal)

    if is_pdf == "pdf":
        form.doc_file(driver).send_keys("D:\\local\\digi\\file\\report.pdf")
    else:
        form.doc_file(driver).send_keys("D:\\local\\digi\\file\\image.jpeg")
    delay(4)
    form.doc_submit(driver).click()
    delay(2)


def test_emet_exceptpdf(driver):
    """unggah dokumen selain pdf"""
    test_doc_upload(driver, is_pdf='image')


def test_emet_pengaturan(driver, **kwargs):
    is_next = kwargs.get('is_next', False)
    is_not_locked = kwargs.get('is_not_locked', False)
    test_doc_upload(driver)

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    if is_next is True:
        if is_not_locked is True:
            doc.btn_add_sign(driver).click()

        doc.btn_send_doc(driver).click()
        delay(1)
        doc.btn_process_send_doc(driver).click()

        try:
            assert doc.icon_x_swal(driver) is not None
        except Exception as error:
            print(error)

        delay(3)
    else:
        try:
            assert doc.canvas(driver) is not None
            delay(1)
        except Exception as error:
            print(error)
        delay(2)


def test_check_kinddoc(driver):
    test_doc_upload(driver)

    assert doc.select_document_type(driver) is not None


def test_select_doc_type(driver, **kwargs):
    employee_acc = kwargs.get('employee_acc', True)
    test_doc_upload(driver, seal=employee_acc)

    if employee_acc:
        doc.check_materai(driver).click()
        Select(doc.select_document_type(driver)).select_by_value("4b")
    else:
        doc.check_materai_personal_acc(driver).click()
        Select(doc.select_document_type(driver)).select_by_value("4b")

    delay(3)

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    assert doc.canvas(driver) is not None
    delay(1.5)


def test_select_doc_type_personal(driver):
    test_select_doc_type(driver, employee_acc=False)


def test_kinddoc_not_selected(driver):
    test_doc_upload(driver, seal=True)

    doc.check_materai(driver).click()

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    assert doc.swal_kinddoc(driver) is not None
    delay(2)


def test_form_receiver(driver):
    test_select_doc_type(driver)


def test_add_new_receiver(driver):
    test_doc_upload(driver, seal=True)

    doc.button_add_receiver(driver).click()

    assert doc.input_email_receiver_2(driver) is not None
    delay(3)


def test_form_not_filled(driver):
    test_doc_upload(driver, seal=True)

    doc.check_materai(driver).click()
    Select(doc.select_document_type(driver)).select_by_value('4b')

    doc.btn_detail_doc(driver).click()
    delay(2)


def test_meterai_occured(driver, **kwargs):
    multiple = kwargs.get('multiple', False)
    count = kwargs.get('count', 0)
    nothing = kwargs.get('nothing', False)

    test_doc_upload(driver, seal=True)

    doc.check_materai(driver).click()
    Select(doc.select_document_type(driver)).select_by_value('4b')

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    if multiple is False:
        doc.button_add_meterai(driver).click()
    else:
        for i in range(count):
            doc.button_add_meterai(driver).click()
            ActionChains(driver).drag_and_drop_by_offset(doc.meterai_zone1(driver), 100, 50).perform()

    if nothing:
        doc.btn_send_doc(driver).click()
        doc.btn_process_send_doc(driver).click()

    delay(7)

    try:
        assert doc.meterai_zone1(driver) is not None
    except Exception as err:
        print(err)


def test_meterai_multiple(driver):
    test_meterai_occured(driver, multiple=True, count=3)


def test_nothing_meterai(driver):
    test_meterai_occured(driver, multiple=False, nothing=True)


def test_not_lock_meterai(driver):
    test_meterai_occured(driver, multiple=False)

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    delay(2)

    try:
        assert doc.swal(driver) is not None
    except Exception as err:
        print(err)


def test_sign_occurred(driver):
    test_meterai_occured(driver, multiple=False)
    doc.cancel_meterai1(driver).click()

    doc.btn_add_sign(driver).click()

    try:
        assert doc.sign_zone_1(driver) is not None
    except Exception as err:
        print(err)


def test_location_sign(driver):
    test_doc_upload(driver)

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    doc.btn_add_sign(driver).click()
    doc.lock_sign_1(driver).click()
    doc.btn_set_email(driver).click()

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    delay(10)


# WEB-3.13
def test_choose_location_sign(driver):
    test_doc_upload(driver)

    doc.button_add_me(driver).click()
    doc.email_first_receiver(driver).clear()
    doc.email_first_receiver(driver).send_keys("dstest1@tandatanganku.com")

    doc.btn_detail_doc(driver).click()
    doc.btn_add_sign(driver).click()
    doc.lock_sign_1(driver).click()
    doc.btn_set_email(driver).click()

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    delay(2)

    doc.button_swal_confirm_ok(driver).click()


def test_nothing_sign(driver):
    test_nothing_meterai(driver)

    try:
        text_null = doc.swal(driver).text
        assert text_null == "Tandatangan tidak boleh kosong"
    except Exception as e:
        print(e)
        print("lempar ke Except")


def test_meterai_overlap(driver, **kwargs):
    sign_overlap = kwargs.get('sign_overlap', False)
    test_doc_upload(driver)

    doc.check_materai(driver).click()
    Select(doc.select_document_type(driver)).select_by_value("4b")

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    if not sign_overlap:
        for i in range(2):
            doc.button_add_meterai(driver).click()

        ActionChains(driver).drag_and_drop_by_offset(doc.meterai_zone1(driver), 100, 20).perform()
        ActionChains(driver).drag_and_drop_by_offset(doc.meterai_zone2(driver), 100, 30).perform()

        doc.button_lock_meterai1(driver).click()
        doc.button_lock_meterai2(driver).click()
    else:
        doc.button_add_meterai(driver).click()
        doc.btn_add_sign(driver).click()

        ActionChains(driver).drag_and_drop_by_offset(doc.meterai_zone1(driver), 100, 0).perform()
        ActionChains(driver).drag_and_drop_by_offset(doc.sign_zone_1(driver), 100, 100).perform()

        doc.button_lock_meterai1(driver).click()
        doc.lock_sign_1(driver).click()
        doc.btn_set_email(driver).click()

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()
    delay(2)

    try:
        text = doc.swal(driver).text
        if sign_overlap:
            assert text == "Lokasi e-Meterai sebaiknya diposisikan secara berdampingan dan tidak tumpang tindih."
        else:
            assert text == "Kotak saling irisan"
    except Exception as e:
        print(e)


def test_meterai_overlap_with_sign(driver):
    test_meterai_overlap(driver, sign_overlap=True)


def test_location_seal(driver, **kwargs):
    used = kwargs.get('used', False)
    test_doc_upload(driver, seal=True)

    Select(doc.select_email_seal(driver)).select_by_visible_text("wahyu@digi-id.id")
    doc.check_materai(driver).click()
    Select(doc.select_document_type(driver)).select_by_value("4b")

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    if not used:
        doc.button_lockseal(driver).click()

        doc.btn_send_doc(driver).click()
        doc.btn_process_send_doc(driver).click()

        delay(3)


def test_location_seal_overlap_meterai(driver):
    test_location_seal(driver, used=True)

    doc.button_lockseal(driver).click()
    doc.button_add_meterai(driver).click()

    ActionChains(driver).drag_and_drop_by_offset(doc.seal_zone(driver), 0, 50).perform()

    doc.button_lock_meterai1(driver).click()

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()
    delay(2)

    try:
        text = doc.swal(driver).text
        assert text == "Lokasi e-Meterai sebaiknya diposisikan secara berdampingan dan tidak tumpang tindih."
    except Exception as e:
        print(e)

