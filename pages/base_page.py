"""
Base Page Object

This module contains the base page object class with common methods
for interacting with web elements.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging


class BasePage:
    """
    Base page object class with common methods for all page objects.
    Provides common functionality for interaction with web elements.
    """
    
    def __init__(self, driver, logger):
        """
        Initialize the base page with driver and logger.
        
        Args:
            driver: Selenium WebDriver instance
            logger: Logging instance
        """
        self.driver = driver
        self.logger = logger
        self.timeout = 15
    
    def find_element(self, locator):
        """
        Find single element with exception handling.
        
        Args:
            locator: Tuple of (By.*, value)
            
        Returns:
            WebElement
        """
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator):
        """Find multiple elements."""
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        """Click on element with explicit wait and JS fallback."""
        try:
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                self.logger.debug(f"Clicked element: {locator}")
                return
            except:
                pass
            
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.debug(f"Clicked element via JS: {locator}")
            
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {str(e)}")
            raise
    
    def type_text(self, locator, text):
        """Type text into input field using JavaScript."""
        try:
            time.sleep(1)
            
            if isinstance(locator, tuple) and locator[0] == By.NAME:
                name = locator[1]
                js_code = """
                var elem = document.querySelector('input[name="' + arguments[0] + '"]');
                if(elem) {
                    elem.value = arguments[1];
                    elem.dispatchEvent(new Event('input', {bubbles: true}));
                    return 'success';
                }
                return 'not_found';
                """
                result = self.driver.execute_script(js_code, name, text)
                
                if result == 'success':
                    self.logger.debug(f"Typed text into input with name '{name}'")
                    return
            
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            self.logger.debug(f"Typed text into: {locator}")
            
        except Exception as e:
            self.logger.error(f"Failed to type text in {locator}: {str(e)}")
            raise
    
    def get_text(self, locator):
        """Get text from element."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.text
        except Exception as e:
            self.logger.error(f"Failed to get text from {locator}: {str(e)}")
            raise
    
    def is_element_visible(self, locator):
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator):
        """Check if element is present in DOM."""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def take_screenshot(self, filename):
        """Take screenshot of current state."""
        try:
            self.driver.save_screenshot(filename)
            self.logger.debug(f"Screenshot saved: {filename}")
        except Exception as e:
            self.logger.warning(f"Failed to take screenshot: {str(e)}")
    
    def wait_for_page_load(self):
        """Wait for page to load completely."""
        time.sleep(2)
    
    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)
        self.logger.info(f"Navigated to: {url}")
        self.wait_for_page_load()
    
    def get_current_url(self):
        """Get current URL."""
        return self.driver.current_url
    
    def wait_for_url_contains(self, text, timeout=10):
        """Wait for URL to contain specific text."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            return True
        except TimeoutException:
            return False