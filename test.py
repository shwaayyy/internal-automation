import time
import re

from datetime import datetime, timedelta
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
