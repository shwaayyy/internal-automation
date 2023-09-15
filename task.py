import os
from typing import Union
from conftest import url, delay
import requests

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from object import *

doc = doc_object
form = form_object
mail = mail_object
url_mail = url["mail-testing"]

wsl_path = "\\wsl$\\Ubuntu\\home\\knowsmore\\airflow\\digi-auto\\digi\\file"
windows_path = "C:\\wahyu\\local\\digi\\file"





def test_upload_doc(driver, **kwargs):
    """Unggah Dokumen PDF"""
    size = kwargs.get('size', '500kb')
    is_personal = kwargs.get('cred', 1)

