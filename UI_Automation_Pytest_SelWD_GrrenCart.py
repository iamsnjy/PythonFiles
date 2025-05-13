import pytest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

@pytest.fixture
def headless_run_fixture():
    chro_opt=webdriver.ChromeOptions()
    chro_opt.add_argument("--headless--")
    yield chro_opt



@pytest.fixture
def setup_teardown(headless_run_fixture):
    chro_opt=headless_run_fixture
    driver=webdriver.Chrome(options=chro_opt)
    driver.implicitly_wait(5)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.fullscreen_window()
    yield driver
    time.sleep(1)
    driver.close()
    driver.quit()

@pytest.mark.parametrize("item",['brocolli','Apple','orange','grapes','water melon'])
def testcase1_add_items_to_cart(setup_teardown,item):
    driver=setup_teardown
    search_box = driver.find_element('css selector', "input[type='search']")
    search_box.click()
    #time.sleep(0.5)

    # Search for an item and add to cart :
    search_box.send_keys(item)
    time.sleep(0.5)

    quantity = driver.find_element('class name', "quantity")
    quantity.clear()
    quantity.send_keys('5')
    #time.sleep(0.5)

    # add item to Cart  using ActionChain :
    add_to_cart_button = driver.find_element('xpath', "//button[text()='ADD TO CART']")
    top_deals = driver.find_element(By.LINK_TEXT, "Top Deals")
    flight_bookings = driver.find_element(By.PARTIAL_LINK_TEXT, "Flight")

    ac = webdriver.ActionChains(driver)
    #ac.move_to_element(add_to_cart_button).perform()
    #time.sleep(0.5)
    #ac.move_to_element(top_deals).perform()
    #time.sleep(0.5)
    #ac.move_to_element(flight_bookings).perform()
    #time.sleep(0.5)
    ac.move_to_element(add_to_cart_button).click().perform()

    driver.find_element(By.CLASS_NAME, "cart-icon").click()

    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

























