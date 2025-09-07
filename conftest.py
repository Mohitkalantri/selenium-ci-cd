import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_options():
    options = Options()
    # Use headless mode in CI; remove it for local debugging
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return options

@pytest.fixture(scope="function")
def driver():
    """Sets up and tears down the Selenium WebDriver for each test function."""
    opts = get_chrome_options()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=opts)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attaches a screenshot to the Allure report if a test fails."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver", None)
        if driver_fixture:
            try:
                png = driver_fixture.get_screenshot_as_png()
                allure.attach(png, name="screenshot", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass

@pytest.fixture(scope="session")
def base_url():
    """Provides the base URL from an environment variable."""
    return os.getenv("TARGET_URL", "https://example.com")