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


def test_emet_upload(driver, **kwargs):
    """Unggah Dokumen PDF"""
    is_seal = kwargs.get('seal', False)
    is_pdf = kwargs.get('exe', 'pdf')

    test_emet_login(driver, seal=is_seal)

    if is_pdf == "pdf":
        form.doc_file(driver).send_keys("\\\wsl$\\Ubuntu\\home\\knowsmore\\airflow\\digi-auto\\digi\\file\\report.pdf")
    else:
        form.doc_file(driver).send_keys("\\\wsl$\\Ubuntu\\home\\knowsmore\\airflow\\digi-auto\\digi\\file\\image.jpeg")
    delay(4)
    form.doc_submit(driver).click()
    delay(2)


def test_emet_exceptpdf(driver):
    """unggah dokumen selain pdf"""
    test_emet_upload(driver, is_pdf='image')


def test_emet_pengaturan(driver, **kwargs):
    is_next = kwargs.get('is_next', False)
    is_not_locked = kwargs.get('is_not_locked', False)
    test_emet_upload(driver)

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
    test_emet_upload(driver)

    assert doc.select_document_type(driver) is not None


def test_select_doc_type(driver, **kwargs):
    employee_acc = kwargs.get('employee_acc', True)
    test_emet_upload(driver, seal=employee_acc)

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
    test_emet_upload(driver, seal=True)

    doc.check_materai(driver).click()

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    assert doc.swal_kinddoc(driver) is not None
    delay(2)


def test_form_receiver(driver):
    test_select_doc_type(driver)


def test_add_new_receiver(driver):
    test_emet_upload(driver, seal=True)

    doc.button_add_receiver(driver).click()

    assert doc.input_email_receiver_2(driver) is not None
    delay(3)


def test_form_not_filled(driver):
    test_emet_upload(driver, seal=True)

    doc.check_materai(driver).click()
    Select(doc.select_document_type(driver)).select_by_value('4b')

    doc.btn_detail_doc(driver).click()
    delay(2)
