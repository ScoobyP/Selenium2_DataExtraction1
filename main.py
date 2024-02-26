from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get('https://www.flipkart.com')
driver.maximize_window()

# Finding the electronics option and hovering on it

electronics_option = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      '/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div[2]/div/div/span')))
hover_electronics = ActionChains(driver).move_to_element(electronics_option)
hover_electronics.perform()

# Hover over the laptop and desktop option

laptopdesktop_option = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/object/a[8]')))
hover_laptopdesktop = ActionChains(driver).move_to_element(laptopdesktop_option)
hover_laptopdesktop.perform()

# Hover and click on 'Laptops' option

laptop_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/object/a[2]')))
hover_laptop_option = ActionChains(driver).move_to_element(laptop_option)
hover_laptop_option.perform()

try:
    laptop_option.click()
except:
    laptop_option2 = driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/object/a[2]')
    laptop_option2.click()

# Saving the Main Laptop page URL in variable

laptop_page = driver.current_url
time.sleep(2)

button_locator = (By.CLASS_NAME, '_1xCO19')

sec = 1

# running OUTER LOOP to get into various sections
while True:
    if sec != 1:
        driver.get(laptop_page)
        print('Laptop Main Page loaded')
        time.sleep(3)

    laptop_sections = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(button_locator))

    section = laptop_sections[sec - 1]
    print('Loop start')

    try:
        section.click()

    except:
        laptop_sections = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(button_locator))
        section = laptop_sections[sec - 1]
        section.click()

    print(sec, 'Section CLICKED')

    time.sleep(2)

    page = 1

    # running INNER LOOP to get to various pages of the sections and fetching data

    while True:
        data = driver.page_source

        print('Page: ', page, 'data extracted')
        with open('flipkart_laptops.html', 'a', encoding='utf-8') as f:
            f.write(data)

        try:
            next_element_loc = (By.LINK_TEXT, 'NEXT')
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(next_element_loc))
            next_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(next_element_loc))
            print('Next button found')
            print(next_button.is_displayed())
            next_button.click()
            print('Next button CLICKED')
            time.sleep(1)

            page += 1

        except:
            print('Next button NOT found')
            break

    if sec == len(laptop_sections):
        break
    else:
        sec += 1
        print('Sec: ', sec)
        continue

print('About to QUIT in ...3,2,1 ')
driver.quit()
