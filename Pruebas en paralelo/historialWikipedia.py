from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

browsers = [
    webdriver.ChromeOptions(),
    webdriver.FirefoxOptions(),
    webdriver.EdgeOptions()
]

@pytest.mark.parametrize("browser_options", browsers)
def test_history_section(browser_options):
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub", options=browser_options)
    try:
        # Navegar a la página de Selenium en Wikipedia
        driver.get("https://es.wikipedia.org/wiki/Selenium")
    
        # Acceder al historial de la página 
        history_link = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "ca-history")))
        
        #Hacer clic sobre el elemento id=ca-history
        history_link.click()
        print("URL después del clic:", driver.current_url)  
        
        # Validar que es la página de historial 
      #  WebDriverWait(driver, 30).until(EC.url_contains("action=history"))
        # Esperar y validar URL
        WebDriverWait(driver, 30).until(EC.url_matches(r"https://.*/w/index.php\?title=.*&action=history"))
        assert "action=history" in driver.current_url
        
        # Validar el título de la página de historial 
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "mw-history-legend")))
        assert "Historial" in driver.title

    finally:
        driver.quit()