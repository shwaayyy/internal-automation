import base64
from datetime import datetime

# import pyautogui
import pytest
import time
from jinja2 import Environment, FileSystemLoader

# from datetime import datetime
from pytest_html import extras

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = {
    "prod": "https://app.digisign.id",
    "app": "https://app.tandatanganku.com",
    "mail-testing": "https://mail.tandatanganku.com",
    "mail-digi": "https://mail.digi-id.id",
    "devkube": "https://devkube.tandatanganku.com",
}

qa_team = {
    "wahyu": "Wahyu Hidayat",
    "aisy": "Rohadatul Aisy",
    "latifah": "Latiah Ramadhana M.E."
}


# robot = pyautogui


def delay(sec):
    time.sleep(sec)


def driver_manager(driver):
    if driver == "chrome":
        options = Options()
        options.add_argument('--use-fake-ui-for-media-stream')
        options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument('--use-fake-device-for-media-stream')
        return webdriver.Chrome(options=options)
    elif driver == "firefox":
        return webdriver.Firefox()


# How to run test you can run with CLI: pytest --html=reports/report.html --self-contained-html test.py
@pytest.fixture
def driver():
    browser = driver_manager("firefox")

    browser.maximize_window()
    browser.implicitly_wait(20)
    browser.get(url["devkube"])

    yield browser

    browser.close()


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "Digisign automation Report"


def pytest_html_results_summary(prefix, summary, postfix):
    # Customize the summary here
    # with open("reports/summary_template.html", "r") as file:
    #     contents = file.read()
    # summary.insert(1, contents)

    # configure Jinja2 environment
    env = Environment(loader=FileSystemLoader('./reports/'))
    template = env.get_template('summary_template.html')

    # Render the templated with the data
    rendered_summary = template.render(qa_name=qa_team["wahyu"], time_test=datetime.now(), env_test=url["devkube"])

    # Insert the rendered summary onti the pytest HTML report
    summary.insert(1, rendered_summary)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.outcome != "passed":
        browser = item.funcargs.get('driver')

        if browser is not None:
            try:
                screenshot = browser.get_screenshot_as_png()
                screenshot_b64 = base64.b64encode(screenshot).decode("utf-8", "ignore")
                extra.append(extras.image(screenshot_b64, "Screenshot"))
            except Exception as e:
                print("Couldn't get screenshot")
                print(e)
        else:
            print("No 'driver' key found in item.funcargs")

    report.extra = extra
