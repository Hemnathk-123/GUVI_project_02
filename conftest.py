"""
Pytest Configuration and Fixtures

This module provides pytest fixtures for browser setup, teardown,
and various test utilities. It also includes hooks for reporting.
"""

import pytest
import logging
import os
from datetime import datetime


class TestConfig:
    """Test configuration manager."""
    
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    ADMIN_USERNAME = "Admin"
    ADMIN_PASSWORD = "admin123"
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30
    SCREENSHOT_DIR = "screenshots"
    REPORT_DIR = "reports"
    TEST_DATA_DIR = "test_data"


@pytest.fixture(scope="session")
def config():
    """Provide test configuration."""
    return TestConfig()


@pytest.fixture(scope="session")
def browser_options(config):
    """Setup browser options for Chrome."""
    from selenium.webdriver.chrome.options import Options
    
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options


@pytest.fixture(scope="function")
def driver(browser_options):
    """Create and provide WebDriver instance."""
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
    
    logging.info("Initializing WebDriver...")
    driver = None
    
    try:
        driver = webdriver.Chrome(options=browser_options)
        driver.implicitly_wait(TestConfig.IMPLICIT_WAIT)
        driver.set_page_load_timeout(TestConfig.PAGE_LOAD_TIMEOUT)
        logging.info("WebDriver initialized successfully")
        yield driver
    except Exception as e:
        logging.error(f"Failed to initialize WebDriver: {str(e)}")
        raise
    finally:
        logging.info("Closing WebDriver...")
        if driver is not None:
            try:
                driver.quit()
            except Exception as e:
                logging.warning(f"Error while closing driver: {str(e)}")


@pytest.fixture(scope="function")
def logger(request):
    """Provide logger for test execution."""
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"logs/test_execution_{test_name}_{timestamp}.log"
    
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    yield logger
    
    logger.info(f"Test {test_name} completed")


@pytest.fixture(scope="function")
def setup_test(driver, logger):
    """Setup before each test."""
    logger.info("=" * 50)
    logger.info("Starting new test execution")
    logger.info("=" * 50)
    yield
    logger.info("Test execution completed")


def pytest_configure(config):
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "positive: Positive test cases")
    config.addinivalue_line("markers", "negative: Negative test cases")
    config.addinivalue_line("markers", "smoke: Smoke tests")
    config.addinivalue_line("markers", "regression: Regression tests")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Add custom summary to terminal output."""
    terminalreporter.write_sep("=", "Test Execution Summary")
    
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    total = passed + failed + skipped
    
    terminalreporter.write_line(f"Total Tests: {total}")
    terminalreporter.write_line(f"Passed: {passed}")
    terminalreporter.write_line(f"Failed: {failed}")
    terminalreporter.write_line(f"Skipped: {skipped}")