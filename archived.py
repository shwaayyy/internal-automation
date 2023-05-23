#



# def test_web2_5_3(driver):
#     """Penentuan lokasi segel pada dokumen"""
#     test_web2_5_1(driver)
#
#     ActionChains(driver).drag_and_drop_by_offset(doc.imgsealer(driver), 100, 100).perform()
#     delay(3)
#
#     doc.button_lockseal(driver).click()
#     doc.btn_send_doc(driver).click()
#     doc.btn_process_send_doc(driver).click()
#
#     doc.confirm_after_send_doc(driver).click()
#
#     delay(5)
# def test_web2_11(driver):
#     """Document yang berhasil di request akan mengirim notif"""
#     test_web2_6_1(driver, pos=[0, 0], size=[0, 0])
#     time_after_test = datetime.now()
#
#     driver.execute_script("window.open('about:blank','tab2')")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get(url_mail)
#
#     mail.input_username(driver).send_keys("ditest6@tandatanganku.com")
#     mail.input_password(driver).send_keys("ditest123" + Keys.ENTER)
#     delay(5)
#
#     for i in range(5):
#         mail.refresh(driver).click()
#         delay(1)
#
#     ActionChains(driver).double_click(mail.msg_list_1(driver)).perform()
#
#     date_received = mail.date_get(driver).text
#     cvrt_date_received = datetime.strptime(date_received, "%B %d, %Y %I:%M %p")
#
#     try:
#         if cvrt_date_received <= time_after_test:
#             print("\nTime send documents is below than email received")
#         else:
#             raise Exception("\nThe message date is not more than now")
#     except Exception as e:
#         print(e)
#
#     delay(2)
#
#
# def test_web2_12(driver):
#     """Dokumen yang berhasil di request akan tampil pada list inbox dari penerima"""
#     form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#     delay(2)
#     form.password(driver).send_keys("Coba1234" + Keys.ENTER)
#     delay(4)
#
#     doc.kotak_masuk_terakhir(driver).click()
#     tanggal_masuk = doc.tanggal_kotak_masuk(driver).text.split("\n")[1]
#
#     print(tanggal_masuk, "tanggal_masuk")
#
#     if bool(re.search('[a-zA-Z]', tanggal_masuk)) is True:
#         date_time_obj = datetime.strptime(tanggal_masuk, "%d %b")
#         yesterday = datetime.now() - timedelta(days=1)
#
#         if datetime.now() >= date_time_obj > yesterday:
#             delay(2)
#         else:
#             raise Exception("This not newest doc")
#     else:
#         date_time_obj = datetime.strptime(tanggal_masuk, "%H:%M").time()
#
#         if datetime.now().time() >= date_time_obj:
#             delay(2)
#         else:
#             raise Exception("This not newest doc")
#
#     doc.latest_tandatangan(driver).click()
#
#     try:
#         assert doc.canvas(driver) is not None
#         delay(2)
#     except Exception as e:
#         print(e)
#
#
# def test_web3_1(driver):
#     """Masuk ke dokumen yang ingin di tandatangani"""
#     form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#     form.password(driver).send_keys("Coba1234", Keys.ENTER)
#
#     delay(2)
#
#     doc.need_sign(driver).click()
#     first = time.time()
#     doc.latest_inbox(driver).click()
#     last = time.time() - first
#
#     delay(4)
#     print(f"\ntime to open doc {time.strftime('%H:%M:%S', time.gmtime(last))}")
#
#
# def test_web3_2(driver):
#     """Masuk ke dokumen yang ingin di lihat"""
#     form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#     form.password(driver).send_keys("Coba1234", Keys.ENTER)
#     delay(2)
#
#     doc.dropdown_dokumen(driver).click()
#     doc.link_terkirim(driver).click()
#
#     doc.btn_eye(driver).click()
#     delay(2)
#
#     try:
#         assert doc.canvas(driver) is not None
#     except Exception as e:
#         raise e
#
#
# def test_web3_3(driver, **kwargs):
#     """Tidak menyetujui Proses tanda tangan"""
#     denial = kwargs.get("denial", True)
#     test_web3_1(driver)
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#
#     if denial:
#         doc.label_tidak(driver).click()
#
#         delay(3)
#         try:
#             assert doc.text_area_reason(driver) is not None
#             delay(3)
#         except Exception as e:
#             raise e
#     else:
#         doc.label_iya(driver).click()
#
#
# def test_web3_4(driver, **kwargs):
#     """Tidak mengisi Kode OTP """
#     otp = kwargs.get('otp_code', "")
#     test_web3_1(driver)
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#
#     doc.btn_otp_email(driver).click()
#
#     doc.otp_input_number(driver).send_keys(otp)
#     delay(3)
#
#     doc.btn_prosign(driver).click()
#     doc.btn_saya_yakin(driver).click()
#     delay(3)
#
#     try:
#         assert doc.swal_otp_none(driver) is not None
#         delay(2)
#     except Exception as e:
#         raise e
#
#
# def test_web3_5(driver):
#     """OTP Salah"""
#     test_web3_4(driver, otp_code="892389")
#
#
# def test_web3_6(driver, **kwargs):
#     """OTP Email pada saat menandatangani dokumen"""
#     # semi-automation because its receiving and sending otp Email
#     otp_auto_use = kwargs.get("otp_auto_use", False)
#
#     if otp_auto_use is False:
#         form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#         form.password(driver).send_keys("Coba1234" + Keys.ENTER)
#         doc.need_sign(driver).click()
#         doc.latest_inbox(driver).click()
#
#         doc.button_proses_sign_one(driver).click()
#         doc.btn_otp_email(driver).click()
#
#     driver.execute_script("window.open('about:blank','tab2')")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get(url_mail)
#
#     mail.input_username(driver).send_keys("ditest6@tandatanganku.com")
#     mail.input_password(driver).send_keys("ditest123" + Keys.ENTER)
#     delay(5)
#
#     for i in range(7):
#         mail.refresh(driver).click()
#         delay(1)
#
#     ActionChains(driver).double_click(mail.msg_list_1(driver)).perform()
#
#     driver.switch_to.frame(mail.iframe_main_body(driver))
#     otp = mail.otp_selector(driver).text
#
#     driver.switch_to.window(driver.window_handles[0])
#
#     doc.otp_input_number(driver).send_keys(otp)
#
#     doc.btn_prosign(driver).click()
#     delay(2)
#     doc.btn_saya_yakin(driver).click()
#     delay(10)
#
#
# def test_web3_8(driver):
#     """Menolak dokumen untuk ditandatangani"""
#     # semi-automation because its receiving and sending otp
#     test_web3_3(driver)
#
#     doc.text_area_reason(driver).send_keys("testing")
#     doc.btn_otp_email(driver).click()
#
#     test_web3_6(driver, otp_auto_use=True)
#
#
# def test_web3_9(driver):
#     """Menyetujui dokumen untuk di tandatangani"""
#     test_web3_3(driver, denial=False)
#
#     doc.btn_otp_email(driver).click()
#     delay(2)
#
#     test_web3_6(driver, otp_auto_use=True)
#
#
# def test_web3_10(driver, **kwargs):
#     """Menyetujui dokumen untuk di tandatangani"""
#     used = kwargs.get("used", False)
#     is_tab3 = kwargs.get("is_tab", True)
#     is_open_mail = kwargs.get("is_open_mail", True)
#     if used is False:
#         test_web3_9(driver)
#     datetime_test = datetime.now()
#
#     if is_tab3:
#         driver.execute_script("window.open('about:blank','tab3')")
#         driver.switch_to.window(driver.window_handles[2])
#         driver.get(url_mail)
#     else:
#         driver.execute_script("window.open('about:blank','tab2')")
#         driver.switch_to.window(driver.window_handles[1])
#         driver.get(url_mail)
#
#     if is_open_mail is False:
#         mail.input_username(driver).send_keys("ditest6@tandatanganku.com")
#         mail.input_password(driver).send_keys("ditest123" + Keys.ENTER)
#         delay(5)
#
#     for i in range(5):
#         mail.refresh(driver).click()
#         delay(1)
#
#     ActionChains(driver).double_click(mail.msg_list_1(driver)).perform()
#
#     date_received = mail.date_get(driver).text
#     cvrt_date_received = datetime.strptime(date_received, "%B %d, %Y %I:%M %p")
#
#     try:
#         if cvrt_date_received <= datetime_test:
#             print("\nTime send documents is below than email received")
#         else:
#             raise Exception("\nThe message date is not more than now")
#     except Exception as e:
#         print(e)
#
#     delay(2)
#
#
# def test_web4_1(driver):
#     """Masuk ke dokumen yang ingin di paraf"""
#     test_web2_3_4(driver, corp=True, full=True)
#
#     driver.execute_script("window.open('about:blank','tab2')")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get(url_staging)
#
#     doc.need_sign(driver).click()
#     doc.latest_inbox(driver).click()
#
#     try:
#         assert doc.canvas(driver) is not None
#         delay(2)
#     except Exception as e:
#         raise e
#
#
# def test_web4_2(driver, **kwargs):
#     """OTP Salah"""
#     otp = kwargs.get('otp_code', "002383")
#     otp_type = kwargs.get('otp_type', "email")
#     semi_automation = kwargs.get('semi_automation', False)
#
#     if otp_type is "email":
#         form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#         form.password(driver).send_keys("Coba1234", Keys.ENTER)
#         delay(2)
#     elif otp_type is "sms":
#         form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
#         form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
#         doc.choose_account(driver).click()
#         delay(2)
#
#     doc.need_sign(driver).click()
#     doc.latest_inbox(driver).click()
#     delay(4)
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#
#     if otp_type == "email":
#         doc.btn_otp_email(driver).click()
#         if semi_automation is False:
#             doc.otp_input_number(driver).send_keys(otp)
#             delay(7)
#
#             doc.btn_prosign(driver).click()
#             doc.btn_saya_yakin(driver).click()
#         else:
#             test_web3_6(driver, otp_auto_use=True)
#     elif otp_type == "sms":
#         doc.btn_otp_sms(driver).click()
#         if semi_automation is False:
#             doc.otp_input_number(driver).send_keys(otp)
#             delay(10)
#         else:
#             delay(20)
#
#         doc.btn_prosign(driver).click()
#         doc.btn_saya_yakin(driver).click()
#
#     if semi_automation:
#         delay(10)
#     else:
#         delay(5)
#         try:
#             assert doc.swal_otp_none(driver) is not None
#             delay(3)
#         except Exception as e:
#             raise e
#
#
# def test_web4_3(driver):
#     # semi-automation because its receiving and sending otp
#     """OTP Email pada saat paraf dokumen"""
#     delay(100)
#     test_web4_2(driver, semi_automation=True)
#
#
# def test_web4_5(driver, **kwargs):
#     """semi-automation because its receiving and sending otp"""
#     # Menolak dokumen untuk paraf
#     is_used = kwargs.get('used', False)
#     form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#     form.password(driver).send_keys("Coba1234", Keys.ENTER)
#     delay(2)
#
#     doc.need_sign(driver).click()
#     doc.latest_inbox(driver).click()
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#
#     if is_used is False:
#         doc.label_tidak(driver).click()
#         delay(3)
#         doc.text_area_reason(driver).send_keys("testing")
#
#     doc.btn_otp_email(driver).click()
#
#     test_web3_6(driver, otp_auto_use=True)
#
#
# def test_web4_6(driver):
#     """Menyetujui dokumen untuk diparaf"""
#     # Menyetujui dokumen untuk diparaf
#     test_web4_5(driver, used=True)
#
#
# def test_web4_7(driver):
#     test_web4_6(driver)
#     test_web3_10(driver, used=True, is_open_mail=True, is_tab=True)
#
#
# def test_web5_1(driver, **kwargs):
#     """Masuk ke dokumen yang ingin di cek"""
#     is_used = kwargs.get('used', False)
#     otp = kwargs.get('otp_type', "sms")
#
#     if is_used is False:
#         if otp is "sms":
#             form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
#             form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
#             doc.choose_account(driver).click()
#         elif otp is "email":
#             form.username(driver).send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
#             form.password(driver).send_keys("Coba1234", Keys.ENTER)
#
#     delay(2)
#
#     doc.need_sign(driver).click()
#     doc.latest_inbox(driver).click()
#
#     try:
#         assert doc.canvas(driver) is not None
#         delay(2)
#     except Exception as e:
#         raise e
#
#
# def test_web5_2(driver):
#     """OTP Salah"""
#     test_web5_1(driver)
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#     doc.btn_otp_email(driver).click()
#     doc.otp_input_number(driver).send_keys("002383")
#
#     doc.btn_prosign(driver).click()
#     doc.btn_saya_yakin(driver).click()
#
#     try:
#         assert doc.swal_otp_none(driver) is not None
#     except Exception as e:
#         raise e
#
#     delay(5)
#
#
# def test_web5_3(driver, **kwargs):
#     """semi-automation because its receiving and sending otp"""
#     # OTP Email pada saat cek dokumen
#     otp = kwargs.get("otp", "email")
#     is_used = kwargs.get('used', False)
#     denial = kwargs.get('denial', False)
#     test_web5_1(driver, used=is_used, otp_type=otp)
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#
#     if denial is True:
#         doc.label_tidak(driver).click()
#         delay(3)
#         doc.text_area_reason(driver).send_keys("testing")
#
#     if otp is "email":
#         doc.btn_otp_email(driver).click()
#         delay(2)
#
#         test_web3_6(driver, otp_auto_use=True)
#     else:
#         doc.btn_otp_sms(driver).click()
#         delay(20)
#
#         doc.btn_prosign(driver).click()
#         doc.btn_saya_yakin(driver).click()
#
#         delay(7)
#
#
# def test_web5_4(driver, **kwargs):
#     """semi-automation because its receiving and sending otp"""
#     denial = kwargs.get('denial', False)
#     otp = kwargs.get("otp", "sms")
#     test_web2_3_3(driver, seal=True)
#
#     doc.btn_add_sign(driver).click()
#
#     doc.lock_sign_1(driver).click()
#     doc.btn_set_email(driver).click()
#
#     doc.btn_send_doc(driver).click()
#     doc.btn_process_send_doc(driver).click()
#     delay(3)
#     doc.confirm_after_send_doc(driver).click()
#     delay(2)
#
#     doc.link_home(driver).click()
#
#     test_web5_3(driver, otp=otp, used=True, denial=denial)
#
#
# def test_web5_5(driver):
#     """semi-automation because its receiving and sending otp"""
#     test_web5_4(driver, denial=True, otp="email")
#
#
# def test_web5_6(driver):
#     """semi-automation because its receiving and sending otp"""
#     test_web5_4(driver, denial=False, otp="email")
#
#
# def test_web5_7(driver):
#     """semi-automation because its receiving and sending otp"""
#     test_web5_6(driver)
#     test_web3_10(driver, used=True, is_open_mail=True, is_tab=True)
#


# def test_web3_7(driver):
#     """OTP SMS pada saat menandatangani dokumen"""
#     # semi-automation because its receiving and sending otp SMS
#     form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
#     form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
#     doc.choose_account(driver).click()
#     doc.need_sign(driver).click()
#
#     doc.latest_inbox(driver).click()
#
#     doc.button_proses_sign_one(driver).click()
#     doc.btn_otp_sms(driver).click()
#
#     delay(25)
#
#     doc.btn_prosign(driver).click()
#     doc.btn_saya_yakin(driver).click()
#     delay(7)


# def test_web4_4(driver):
#     """OTP SMS pada saat paraf dokumen"""
#     # semi-automation because its receiving and sending otp
#     test_web4_2(driver, semi_automation=True, otp_type="sms")

# def test_web6_1(driver):
#     """all of this is semi-automation test because it's receiving an OTP"""
#     test_web2_5_3(driver)
#
#     driver.execute_script("window.open('about:blank','tab2')")
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get("https://app.tandatanganku.com")
#
#     doc.need_sign(driver).click()
#     doc.latest_inbox(driver).click()
#
#     try:
#         assert doc.canvas(driver) is not None
#     except Exception as e:
#         raise e
#
#     delay(2)
#
#
# def test_web6_2(driver, **kwargs):
#     auto = kwargs.get('auto', True)
#     used = kwargs.get('used', False)
#     denial = kwargs.get('denial', False)
#     otp_type = kwargs.get('otp_type', 'email')
#     form.username(driver).send_keys("wahyuhi" + Keys.ENTER)
#     form.password(driver).send_keys("Kijang321!" + Keys.ENTER)
#     doc.choose_account(driver).click()
#
#     delay(3)
#
#     doc.need_sign(driver).click()
#     doc.latest_inbox(driver).click()
#
#     doc.button_proses_sign_one(driver).click()
#     delay(2)
#
#     if denial is True:
#         doc.label_tidak(driver).click()
#         delay(3)
#         doc.text_area_reason(driver).send_keys("testing")
#
#     if otp_type is "email":
#         doc.btn_otp_email(driver).click()
#     elif otp_type is "sms":
#         doc.btn_otp_sms(driver).click()
#
#     if auto is True:
#         doc.otp_input_number(driver).send_keys("002383")
#     else:
#         delay(25)
#
#     doc.btn_prosign(driver).click()
#     doc.btn_saya_yakin(driver).click()
#
#     if used is False:
#         try:
#             assert doc.swal_otp_none(driver) is not None
#         except Exception as e:
#             raise e
#
#     delay(10)
#
#
# def test_web6_3(driver):
#     test_web6_2(driver, auto=False, used=True, otp_type="sms")
#
#
# def test_web6_4(driver):
#     test_web6_2(driver, auto=False, denial=True, otp_type="sms")
#
#
# def test_web6_5(driver):
#     test_web6_2(driver, auto=False, denial=False, otp_type="sms")
#
#
# def test_web6_6(driver):
#     test_web6_5(driver)
#
#     test_web3_10(driver, used=True)