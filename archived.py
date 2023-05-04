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