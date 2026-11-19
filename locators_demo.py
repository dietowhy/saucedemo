from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    try:
        driver.get("https://www.saucedemo.com/")

        # Основные локаторы
        driver.find_element(By.ID, "user-name")
        driver.find_element(By.NAME, "password")
        driver.find_element(By.CLASS_NAME, "input_error")
        driver.find_element(By.TAG_NAME, "input")

        # XPath
        driver.find_element(By.XPATH, "//input[@id='user-name']")
        driver.find_element(By.XPATH, "//h4[text()='Accepted usernames are:']")
        driver.find_element(By.XPATH, "//input[contains(@id,'user')]")
        driver.find_element(By.XPATH, "//h4[contains(text(),'Accepted')]")
        driver.find_element(By.XPATH, "//input[@id='user-name']/ancestor::div[@class='form_group']")
        driver.find_element(By.XPATH, "//form/descendant::input")
        driver.find_element(By.XPATH, "//input[@id='user-name']/following::input[1]")
        driver.find_element(By.XPATH, "//input[@id='user-name']/parent::div")
        driver.find_element(By.XPATH, "//input[@name='password']/preceding::input[1]")
        driver.find_element(By.XPATH, "//input[@name='user-name' and @type='text']")

        # CSS
        driver.find_element(By.CSS_SELECTOR, ".form_input")
        driver.find_element(By.CSS_SELECTOR, ".input_error.form_input")
        driver.find_element(By.CSS_SELECTOR, ".form_group .form_input")
        driver.find_element(By.CSS_SELECTOR, "#user-name")
        driver.find_element(By.CSS_SELECTOR, "input")
        driver.find_element(By.CSS_SELECTOR, "input.form_input")
        driver.find_element(By.CSS_SELECTOR, "[name='password']")
        driver.find_element(By.CSS_SELECTOR, "[class~='form_input']")
        driver.find_element(By.CSS_SELECTOR, "[name|='user']")
        driver.find_element(By.CSS_SELECTOR, "[id^='user']")
        driver.find_element(By.CSS_SELECTOR, "[id$='name']")
        driver.find_element(By.CSS_SELECTOR, "[id*='ser']")

        #LINK_TEXT / PARTIAL_LINK_TEXT
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Sauce Labs")

        print("OK: все локаторы найдены")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()