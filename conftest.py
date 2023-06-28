import base64
import pyautogui
import pytest
import time

from datetime import datetime
from pytest_html import extras

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = {
    "prod": "https://app.digisign.id",
    "app": "https://app.tandatanganku.com",
    "mail-testing": "https://mail.tandatanganku.com",
    "mail-digi": "https://mail.digi-id.id",
    "dummy": "https://www.jetbrains.com/"
}


qa_team = {
    "wahyu": "Wahyu Hidayat",
    "aisy": "Rohadatul Aisy",
    "latifah": "Latiah Ramadhana M.E."
}

robot = pyautogui


def delay(sec):
    time.sleep(sec)


def driver_manager(driver):
    if driver is "chrome":
        options = Options()
        options.add_argument('--use-fake-ui-for-media-stream')
        options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument('--use-fake-device-for-media-stream')
        return webdriver.Chrome(options=options)
    elif driver is "firefox":
        return webdriver.Firefox()


# How to run the test you can run with CLI: pytest --html=reports/report_reg_wna.html --self-contained-html
# <test_case_file>.py
@pytest.fixture
def driver():
    browser = driver_manager("chrome")

    browser.maximize_window()
    browser.implicitly_wait(20)
    browser.get(url["app"])

    yield browser

    browser.close()


def pytest_configure(config):
    config._metadata.update({
        'PIC': qa_team["wahyu"],
        'Time Test': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    })


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.outcome != "passed":
        browser = item.funcargs['driver']
        try:
            screenshot = browser.get_screenshot_as_png()
            screenshot_b64 = base64.b64encode(screenshot).decode("utf-8", "ignore")
            extra.append(extras.image(screenshot_b64, "Screenshot"))
        except Exception as e:
            print("Couldn't get screenshot")
            print(e)
        report.extra = extra
