import pytest
from selenium.webdriver.common.by import By


def test_cart(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.NAME, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    inventory_item = browser.find_element(By.CSS_SELECTOR, ".inventory_item")
    product_name = inventory_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text.strip()
    product_price = inventory_item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text.strip()

    inventory_item.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()

    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_item = browser.find_element(By.CSS_SELECTOR, ".cart_item")
    cart_name = cart_item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text.strip()
    cart_price = cart_item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text.strip()

    assert cart_name == product_name, (
        f"Название товара в корзине не совпадает: "
        f"'{cart_name}' != '{product_name}'"
    )
    assert cart_price == product_price, (
        f"Цена товара в корзине не совпадает: "
        f"'{cart_price}' != '{product_price}'"
    )