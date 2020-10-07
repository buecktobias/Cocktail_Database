import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_all_cocktails():
    cocktail_url = "https://www.cocktails.de/cocktail-rezepte"
    browser = webdriver.Firefox()
    browser.get(cocktail_url)
    browser.implicitly_wait(2)
    year_button = "/html/body/div[5]/div/div/div/div/div[1]/button"
    wait = WebDriverWait(browser, 10)
    year_button_ob = wait.until(EC.element_to_be_clickable((By.XPATH, year_button)))
    year_button_ob.click()

    for i in range(5_000):
        cocktail_elements = browser.find_elements_by_class_name("recipe-card")
        browser.execute_script("arguments[0].scrollIntoView();", cocktail_elements[-1])
        browser.implicitly_wait(4)
        time.sleep(0.1)
    return browser.find_elements_by_class_name("recipe-card")


def get_cocktail_names():
    cocktail_elements= get_all_cocktails()
    cocktail_names = []
    for cocktail_el in cocktail_elements:
        cocktail_names.append(cocktail_el.find_element_by_class_name("card").get_attribute("title"))
    return cocktail_names


def get_cocktail_links():
    cocktail_elems = get_all_cocktails()
    all_links = []
    for e in cocktail_elems:
        cocktail_link = e.find_element_by_tag_name("a").get_attribute("href")
        all_links.append(cocktail_link)
    return all_links


if __name__ == '__main__':
    print(get_cocktail_names())
