import random
import time
from selenium import webdriver

base_url = 'https://translate.google.sk/?hl=sk&tab=wT#sk/sk/Priprav sa%0A%0A'

def generation_numbers(size=1, count=1):
    list_numbers = []
    for i in range(count):
        number = ''
        for j in range(size):
            if j == 0:
                number += str(random.randint(1, 9))
            else:
                number += str(random.randint(0, 9))
        list_numbers.append(number)
    return list_numbers

def save_testing_numbers(numbers):
    fh = None
    try:
        fh = open('log.txt','a')
        for i, number in enumerate(numbers):
            fh.write(str(i)+' - '+number + '\n')
    except FileNotFoundError as err:
        print('Error File')
    finally:
        if fh is not None:
            fh.close()

def create_google_url(size=1, count=1):
    global numbers
    numbers = generation_numbers(size, count)
    save_testing_numbers(numbers)
    list_urls = []
    delimeter = '%0A'
    url = ''
    for i in range(len(numbers)):
        url = base_url
        for j in range(len(numbers[i])):
                url += str(numbers[i][j]) + delimeter
        list_urls.append(url)
    return list_urls

urls = create_google_url(size=5, count=5)

for i in range(len(urls)):
    driver = webdriver.Chrome()
    driver.get(urls[i])
    time.sleep(1)
    element = driver.find_element_by_css_selector("div[class='trans-listen-button goog-toolbar-button'] span[class='jfk-button-img']")
    element.click()
    time.sleep(10)
    driver.quit()