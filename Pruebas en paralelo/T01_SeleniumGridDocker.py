from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest

browsers = [
    ChromeOptions(),
    FirefoxOptions(),
    EdgeOptions()
]

@pytest.mark.parametrize("browser_options", browsers)
def test_paralelo(browser_options):
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=browser_options)  
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()