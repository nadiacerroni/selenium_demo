import pytest
from selenium.webdriver.common.by import By

expected_title = 'Amazon.com. Spend less. Smile more.'
base_url = 'https://www.amazon.com'
search_title = 'Amazon.com : nike air max'


@pytest.mark.regressiontest
def test_search_airmax(browser):
    # navigate to Amazon.com home page
    browser.get(base_url)
    # verify that web page title is Amazon.com
    assert browser.title == expected_title
    # locate search field element
    search_field = browser.find_element(By.ID, "twotabsearchtextbox")
    # enter "nike air max" in the search field
    search_field.send_keys("nike air max")
    # locate search button
    search_button = browser.find_element(By.XPATH, "//input[@value='Go']")
    # click on 'Search' button
    search_button.click()
    # verify actual page title matches expected page title
    assert browser.title == search_title