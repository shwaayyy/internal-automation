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


def test_web1_1(driver, **kwargs):
    """Unggah Dokumen PDF"""
    is_pdf = kwargs.get('exe', 'pdf')
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
    if is_pdf == "pdf":
        form.doc_file(driver).send_keys("D:\\repository\\try\\PyTest-dev\\src\\file\\report.pdf")
    else:
        form.doc_file(driver).send_keys("D:\\repository\\try\\PyTest-dev\\src\\file\\image.jpeg")
    delay(4)
    form.doc_submit(driver).click()
    delay(2)


def test_web1_2(driver):
    """Unggah Dokumen selain PDF"""
    test_web1_1(driver, exe="img")


def test_web2_1_1(driver, **kwargs):
    """Pengaturan dokumen yang ingin dikirim sesuai"""
    is_next = kwargs.get('is_next', False)
    is_not_locked = kwargs.get('is_not_locked', False)
    test_web1_1(driver)

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


def test_web2_1_2(driver):
    """Pengaturan dokumen yang ingin dikirim tidak sesuai ( sudah lewat dari tanggal sekarang )"""
    test_web1_1(driver)

    doc.btn_choose_expired_date(driver).click()

    for i in range(6):
        doc.btn_previous_month_date(driver).click()
        delay(1)

    doc.date(driver).click()
    doc.button_ok_date(driver).click()

    try:
        assert doc.icon_x_swal(driver) is not None
        delay(3)
    except Exception as error:
        print(error)

    delay(1)


def test_web2_2_1(driver, **kwargs):
    """Tidak isi form penerima dokumen"""
    is_filled = kwargs.get('is_filled', False)
    test_web1_1(driver)

    if is_filled is True:
        doc.name_first_receiver(driver).send_keys("wahyu")
        doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")

    doc.btn_detail_doc(driver).click()
    delay(2)

    if is_filled is False:
        try:
            assert doc.err_name_receiver(driver) is not None
            assert doc.err_email_receiver(driver) is not None
            delay(3)
        except Exception as err:
            print(err)
    else:
        try:
            assert doc.canvas(driver) is not None
            delay(3)
        except Exception as err:
            print(err)


def test_web2_2_2(driver):
    """Isi form penerima dokumen"""
    test_web2_2_1(driver, is_filled=True)


def test_web2_2_3(driver):
    """isi form penerima dokumen dengan nama kosong"""
    test_web1_1(driver)

    doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")
    doc.btn_detail_doc(driver).click()

    try:
        assert doc.err_name_receiver(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(2)


def test_web2_2_4(driver):
    """isi form penerima dokumen dengan spasi saja"""
    test_web1_1(driver)

    doc.name_first_receiver(driver).send_keys(" ")
    doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")
    doc.btn_detail_doc(driver).click()

    try:
        assert doc.err_name_receiver(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(2)


def test_web2_2_5(driver):
    """isi form email penerima kosong"""
    test_web1_1(driver)

    doc.name_first_receiver(driver).send_keys("wahyu")

    doc.btn_detail_doc(driver).click()
    delay(2)

    try:
        assert doc.err_email_receiver(driver) is not None
        delay(3)
    except Exception as err:
        print(err)


def test_web2_2_6(driver):
    """isi form email penerima dengan format email salah"""
    test_web1_1(driver)

    doc.name_first_receiver(driver).send_keys("wayy")
    doc.email_first_receiver(driver).send_keys("ditest28")

    doc.btn_detail_doc(driver).click()
    delay(2)

    try:
        assert doc.err_email_receiver(driver) is not None
        delay(3)
    except Exception as error:
        print(error)


def test_web2_3_1(driver):
    """Mengatur tanda tangan Sesuai urutan dengan urutan dibutuhkan tandatangan di awal"""
    test_web1_1(driver)

    doc.label_sort_sign(driver).click()
    doc.button_add_me(driver).click()

    doc.btn_detail_doc(driver).click()
    delay(2)

    try:
        assert doc.canvas(driver) is not None
        delay(3)
    except Exception as err:
        print(err)


def test_web2_3_2(driver, **kwargs):
    """Mengatur tanda tangan Sesuai urutan dengan urutan dibutuhkan pengecekan di akhir"""
    select = kwargs.get('select', "Dibutuhkan Pengecekan")
    seal = kwargs.get('seal', False)
    test_web1_1(driver, seal=seal)

    doc.button_add_me(driver).click()
    doc.label_sort_sign(driver).click()

    if select is "Dibutuhkan Tandatangan":
        Select(doc.select_action_need(driver)).select_by_visible_text("Dibutuhkan Pengecekan")
    else:
        pass

    doc.button_add_receiver(driver).click()
    doc.input_name_receiver_2(driver).send_keys("Aziz")
    if seal:
        doc.input_email_receiver_2(driver).send_keys("ditest6@tandatanganku.com")
    else:
        doc.input_email_receiver_2(driver).send_keys("aziz@digi-id.id")

    if select is "Dibutuhkan Tandatangan":
        doc.btn_detail_doc(driver).click()
        delay(2)
        try:
            assert doc.canvas(driver) is not None
            delay(3)
        except Exception as err:
            raise err
    elif select is "Dibutuhkan Pengecekan":
        Select(doc.select_action_need_2(driver)).select_by_visible_text(select)
        doc.btn_detail_doc(driver).click()
        delay(2)
        try:
            assert doc.icon_x_swal(driver) is not None
            delay(3)
        except Exception as e:
            raise e


def test_web2_3_3(driver, **kwargs):
    """Mengatur tanda tangan Sesuai urutan dengan urutan dibutuhkan pengecekan di awal"""
    seal = kwargs.get('seal', False)
    test_web2_3_2(driver, select="Dibutuhkan Tandatangan", seal=seal)


def test_web2_3_4(driver, **kwargs):
    """Memilih tindakan dibutuhkan paraf"""
    is_full = kwargs.get('full', False)
    is_corp = kwargs.get('corp', False)
    test_web1_1(driver, seal=is_corp)

    doc.name_first_receiver(driver).send_keys("digi")
    doc.email_first_receiver(driver).send_keys("ditest6@tandatanganku.com")
    Select(doc.select_action_need(driver)).select_by_visible_text("Dibutuhkan Paraf")

    doc.btn_detail_doc(driver).click()

    if is_full is True:
        doc.button_paraf(driver).click()
        delay(2)
        ActionChains(driver).drag_and_drop_by_offset(doc.paraf_box(driver), 10, 100).perform()

        doc.lock_paraf_1(driver).click()
        doc.btn_set_email(driver).click()
        doc.btn_send_doc(driver).click()
        doc.btn_process_send_doc(driver).click()

        doc.confirm_after_send_doc(driver).click()

        delay(5)
    else:
        try:
            assert doc.canvas(driver) is not None
            delay(2)
        except Exception as err:
            print(err)

        delay(2)


def test_web2_4_1(driver):
    """Tidak menentukan lokasi Paraf pada dokumen"""
    test_web2_3_4(driver)

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    try:
        assert doc.sign_null(driver) is not None
    except Exception as err:
        print(err)

    delay(5)


def test_web2_4_2(driver):
    """penentuan lokasi paraf"""
    test_web2_3_4(driver, corp=True)


def test_web2_5_1(driver):
    """Memilih tindakan untuk seal Dokumen"""
    test_web1_1(driver, seal=True)

    Select(doc.select_email_seal(driver)).select_by_visible_text("wahyu@digi-id.id")
    delay(2)

    doc.button_add_me(driver).click()
    doc.btn_detail_doc(driver).click()

    try:
        assert doc.canvas(driver) is not None
    except Exception as err:
        print(err)

    delay(2)


def test_web2_5_2(driver):
    """Tidak menentukan lokasi segel pada dokumen"""
    test_web2_5_1(driver)

    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    try:
        assert doc.sign_null(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(5)


def test_web2_6_1(driver, **kwargs: Union[int, bool, list[int]]):
    """Lokasi tanda tangan dengan ukuran paling kecil (width:107px; height:32px)"""
    iteration = kwargs.get('iteration', 1)
    is_not_seal = kwargs.get('is_not_seal', True)
    is_used = kwargs.get('is_draft', False)
    meterai = kwargs.get('meterai', False)
    size = kwargs.get('size', [-100, -65])
    pos = kwargs.get('pos', [80, 90])

    if is_used is False:
        form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
        delay(2)
        form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
        delay(4)
        doc.choose_account(driver).click()

    for i in range(iteration):
        if is_used is False:
            delay(2)
            form.doc_file(driver).send_keys("D:\\repository\\try\\PyTest-dev\\src\\file\\report.pdf")
            delay(2)
            form.doc_submit(driver).click()
            delay(2)

            if is_not_seal is True:
                doc.check_seal_doc(driver).click()
            else:
                Select(doc.select_email_seal(driver)).select_by_visible_text("wahyu@digi-id.id")

            if meterai:
                doc.check_materai(driver).click()
                Select(doc.select_document_type(driver)).select_by_visible_text("Surat Pernyataan")

            doc.name_first_receiver(driver).send_keys("digisign")
            doc.email_first_receiver(driver).send_keys("dstest1@tandatanganku.com")

        doc.btn_detail_doc(driver).click()
        delay(2)
        doc.btn_add_sign(driver).click()

        delay(4)

        if meterai:
            doc.button_add_meterai(driver).click()
            ActionChains(driver).drag_and_drop_by_offset(doc.kotak_materai(driver), pos[0], pos[1]).perform()
            doc.button_lock_meterai(driver).click()

        ActionChains(driver).drag_and_drop_by_offset(doc.sign_zone_1(driver), pos[0], pos[1]).perform()
        ActionChains(driver).drag_and_drop_by_offset(doc.resizing_zone_1(driver), size[0], size[1]).perform()

        delay(5)

        doc.lock_sign_1(driver).click()
        delay(1)
        doc.btn_set_email(driver).click()
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


def test_web2_6_2(driver):
    """Lokasi tanda tangan dengan ukuran default (width:144px; height:72px)"""
    test_web2_6_1(driver, pos=[20, 78])


def test_web2_6_3(driver):
    """Lokasi tanda tangan dengan ukuran besar (width:331.53px; height:165.76px)"""
    test_web2_6_1(driver, size=[472, 236], pos=[-45, 0])


def test_web2_7(driver):
    """Tidak menentukan lokasi tanda tangan pada dokumen"""
    test_web2_1_1(driver, is_next=True)


def test_web2_8(driver):
    """Tidak mengunci lokasi tandatangan untuk user yang sudah ditentukan"""
    test_web2_1_1(driver, is_not_locked=True, is_next=True)


def test_web2_9(driver):
    """Lokasi tanda tangan di luar kanvas atau keluar dari kanvas"""
    test_web1_1(driver)

    doc.button_add_me(driver).click()

    doc.btn_detail_doc(driver).click()

    doc.btn_add_sign(driver).click()
    ActionChains(driver).drag_and_drop_by_offset(doc.sign_zone_1(driver), 700, 200).perform()
    delay(2)

    doc.lock_sign_1(driver).click()
    doc.btn_set_email(driver).click()
    doc.btn_send_doc(driver).click()
    doc.btn_process_send_doc(driver).click()

    try:
        assert doc.sign_null(driver) is not None
        delay(3)
    except Exception as err:
        print(err)

    delay(2)


# send documents with emeterai

def test_bulk_send(driver):
    """Menyelesaikan Send Dokumen dengan benar dan dengan e-meterai bulksend"""
    test_web2_6_1(driver, meterai=True, iteration=10)


def test_send_doc_meterai(driver):
    """Send document with meterai"""
    test_web2_6_1(driver, meterai=True)

