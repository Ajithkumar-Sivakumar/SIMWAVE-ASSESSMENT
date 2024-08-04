# Add sample CSS and elements and comments to get understand.
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("URL")
    yield driver
    driver.quit()

def test_fill_search_fields(driver):
    # Select duration
    duration_dropdown = Select(driver.find_element(By.ID, "duration"))
    duration_dropdown.select_by_visible_text("30 minutes")

    # Enter topic
    topic_field = driver.find_element(By.ID, "topic")
    topic_field.send_keys("Mathematics")

    # Click search button
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    # Wait for results
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "results")))

    # Verify results or other assertions
    results = driver.find_element(By.ID, "results").text
    assert "Mathematics" in results, "Search results do not contain the topic 'Mathematics'"
