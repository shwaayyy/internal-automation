from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import url, delay

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
mail = mail_object
url_mail = url["mail-testing"]
url_staging = url["test"]

act_kind = {
    "1": "sign",
    "2": "initials",
    "3": "approval",
    "4": "share"
}

credentials = [
    {
        "username": "dstest1@tandatanganku.com",
        "password": "123456789!",
        "pass-email": "dstest123"
    },
    {
        "username": "wahyu@digi-id.id",
        "password": "Kijang321!",
        "pass-email": "Kijang321!"
    },
    {
        "username": "dstest4@tandatanganku.com",
        "password": "123456789!",
        "pass-email": "dstest123"
    },
    {
        "username": "ditest6@tandatanganku.com",
        "password": "Coba1234",
        "pass-email": "ditest123"
    },
]


def test_emet_login(driver, **kwargs: int):
    """test login"""
    seal = kwargs.get('seal', 0)

    form.username(driver).send_keys(credentials[seal]["username"] + Keys.ENTER)
    delay(2)
    form.password(driver).send_keys(credentials[seal]["password"] + Keys.ENTER)
    delay(4)

    if seal == 1:
        doc.choose_account(driver).click()
    elif seal == 0:
        doc.choose_account_personal(driver).click()
    else:
        pass

    delay(3)


def test_doc_upload(driver, **kwargs):
    """Unggah Dokumen PDF"""
    is_seal = kwargs.get('seal', 0)
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
    employee_acc = kwargs.get('employee_acc', 1)
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
    test_select_doc_type(driver, employee_acc=0)


def test_kinddoc_not_selected(driver):
    test_doc_upload(driver, seal=1)

    doc.check_materai(driver).click()

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    assert doc.swal_kinddoc(driver) is not None
    delay(2)


def test_form_receiver(driver):
    test_select_doc_type(driver)


def test_add_new_receiver(driver):
    test_doc_upload(driver, seal=1)

    doc.button_add_receiver(driver).click()

    assert doc.email_receiver(driver, 2) is not None
    delay(3)


def test_form_not_filled(driver):
    test_doc_upload(driver, seal=1)

    doc.check_materai(driver).click()
    Select(doc.select_document_type(driver)).select_by_value('4b')

    doc.btn_detail_doc(driver).click()
    delay(2)


def test_meterai_occured(driver, **kwargs):
    multiple = kwargs.get('multiple', False)
    count = kwargs.get('count', 0)
    nothing = kwargs.get('nothing', False)

    test_doc_upload(driver, seal=1)

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
    doc.email_receiver(driver, 1).clear()
    doc.email_receiver(driver, 1).send_keys("dstest1@tandatanganku.com")

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
    test_doc_upload(driver, seal=1)

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

    doc.button_add_meterai(driver).click()
    ActionChains(driver).drag_and_drop_by_offset(doc.seal_zone(driver), 0, 50).perform()
    doc.button_lockseal(driver).click()

    doc.button_lock_meterai1(driver).click()

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()
    delay(2)

    try:
        text = doc.swal(driver).text
        assert text == "Lokasi e-Meterai sebaiknya diposisikan secara berdampingan dan tidak tumpang tindih."
    except Exception as e:
        print(e)


def action_needed(driver, act: str, sort: int, name="", email=0):
    if act == "sign":
        name = "jajang"
        email = 0
    elif act == "initials":
        name = "garnacho"
        email = 2
    elif act == "approval":
        name = "bagott"
        email = 3
    elif act == "share":
        name = "eko"
        email = 1

    doc.name_receiver(driver, sort).send_keys(name)
    doc.email_receiver(driver, sort).send_keys(credentials[email]["username"])
    Select(doc.select_action(driver, sort)).select_by_value(act)
    delay(2)


def test_one_flow_send_doc(driver, **kwargs):
    """default send doc case test"""

    iteration = kwargs.get('iteration', 1)
    is_seal = kwargs.get('is_seal', 0)
    seq = kwargs.get('seq', False)
    actions = kwargs.get('actions', [{"actions": "sign", "sort": 1}])
    account_num = kwargs.get('account_num', 1)
    is_used = kwargs.get('is_draft', False)
    meterai = kwargs.get('meterai', False)
    size = kwargs.get('size', [-100, -65])
    pos = kwargs.get('pos', [80, 90])
    actions_list = [item["actions"] for item in actions]

    if is_used is False:
        test_emet_login(driver, seal=account_num)

    for i in range(iteration):
        if is_used is False:
            delay(2)
            form.doc_file(driver).send_keys("D:\\local\\digi\\file\\report.pdf")
            delay(2)
            form.doc_submit(driver).click()
            delay(2)

            if account_num == 1:
                if is_seal == 0:
                    doc.check_seal_doc(driver).click()
                else:
                    Select(doc.select_email_seal(driver)).select_by_value(credentials[1]["username"])

            if meterai:
                doc.check_materai(driver).click()
                Select(doc.select_document_type(driver)).select_by_value("4b")

            if seq:
                doc.label_sort_sign(driver).click()

            if len(actions) > 1:
                for n in range(len(actions) - 1):
                    doc.button_add_receiver(driver).click()

                pass

            for act in actions:
                action_needed(driver, act["actions"], act["sort"])

                if act == actions[-1]:
                    doc.btn_detail_doc(driver).click()
                    delay(2)
                else:
                    pass
        else:
            doc.btn_detail_doc(driver).click()
            delay(2)

            doc.btn_add_sign(driver).click()

        if 'sign' in actions_list:
            doc.btn_add_sign(driver).click()
            ActionChains(driver).drag_and_drop_by_offset(doc.sign_zone_1(driver), pos[0], pos[1]).perform()
            doc.lock_sign_1(driver).click()
            doc.btn_set_email(driver).click()

        if 'initials' in actions_list:
            doc.button_paraf(driver).click()
            ActionChains(driver).drag_and_drop_by_offset(doc.paraf_box(driver), pos[0], pos[1]).perform()
            doc.lock_paraf_1(driver).click()

            doc.btn_set_email_paraf(driver).click()
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(
                    doc.btn_set_email_paraf(driver)
                )
            ).click()

        if is_seal:
            ActionChains(driver).drag_and_drop_by_offset(doc.seal_zone(driver), 0, 300).perform()
            doc.button_lockseal(driver).click()

        if meterai:
            doc.button_add_meterai(driver).click()
            ActionChains(driver).drag_and_drop_by_offset(doc.meterai_zone1(driver), pos[0], pos[1]).perform()
            doc.button_lock_meterai1(driver).click()

        doc.btn_send_doc(driver).click()
        doc.btn_process_send_doc(driver).click()
        delay(3)

        if i is len(range(iteration)) - 1:
            pass
            delay(3)
        else:
            doc.confirm_after_send_doc(driver).click()
            delay(3)
            doc.link_home(driver).click()


def test_send_to_email_after_successful(driver):
    test_one_flow_send_doc(driver, meterai=True, account_num=0)

    time_after_test = datetime.now()

    driver.execute_script("window.open('about:blank','tab2')")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url_mail)

    mail.input_username(driver).send_keys(credentials[0]["username"])
    mail.input_password(driver).send_keys(credentials[0]["pass-email"] + Keys.ENTER)
    delay(5)

    for i in range(6):
        mail.refresh(driver).click()
        delay(1)

    ActionChains(driver).double_click(mail.msg_list_1(driver)).perform()

    date_received = mail.date_get(driver).text
    cvrt_date_received = datetime.strptime(date_received, "%B %d, %Y %I:%M %p")

    try:
        if cvrt_date_received <= time_after_test:
            print("\nSuccess send Email and Time send documents is below than email received")
        else:
            raise Exception("\nThe message date is not more than now")
    except Exception as e:
        print(e)

    delay(2)


def test_doc_sent_and_appear_on_inbox(driver):
    test_one_flow_send_doc(driver, meterai=True, account_num=0)

    time_after_send = datetime.now()

    doc.confirm_after_send_doc(driver).click()

    doc.kotak_masuk(driver).click()

    doc.kotak_masuk_terakhir(driver).click()

    date_send = doc.date_send_doc1(driver).text
    time_send_doc = datetime.strptime(date_send, "%d %b %Y %H:%M")

    try:
        if time_send_doc <= time_after_send:
            print("\nSuccess send Doc. Time send documents is below equal than send doc inbox")
        else:
            raise Exception("\nThe message date is not more than now")
    except Exception as e:
        print(e)


def test_send_doc_meterai(driver):
    """Send document with meterai"""
    test_one_flow_send_doc(driver, meterai=True)


def test_send_doc_meterai_paraf(driver):
    """send document with meterai and paraf"""
    test_one_flow_send_doc(driver, meterai=True, actions=[{"actions": "initials", "sort": 1}])


def test_send_doc_meterai_paraf_ttd(driver):
    """send document with meterai and paraf"""
    test_one_flow_send_doc(driver, meterai=True, actions=[
        {"actions": "initials", "sort": 1},
        {"actions": "sign", "sort": 2}
    ])


def test_send_doc_meterai_ttd_share(driver):
    """send document with meterai, tandatangan, dan salinan"""
    test_one_flow_send_doc(
        driver,
        meterai=True,
        actions=[
            {"actions": 'sign', "sort": 1},
            {"actions": 'share', "sort": 2}
        ]
    )


def test_send_doc_emeterai_ttd_check(driver):
    """send document with meterai, ttd, dan cek"""
    test_one_flow_send_doc(
        driver,
        meterai=True,
        seq=True,
        actions=[
            {"actions": 'approval', "sort": 1},
            {"actions": 'sign', "sort": 2}
        ]
    )


def test_send_doc_meterai_sign_seal(driver):
    test_one_flow_send_doc(driver, meterai=True, is_seal=1)


def test_bulk_send(driver):
    """Menyelesaikan Send Dokumen dengan benar dan dengan e-meterai bulksend"""
    test_one_flow_send_doc(driver, meterai=True, iteration=5)
