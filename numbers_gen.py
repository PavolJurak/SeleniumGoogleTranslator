import random
from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver.exe')
base_url = 'https://translate.google.sk/?hl=sk&tab=wT#sk/sk/'

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

def create_google_url(size=1, count=1):
    numbers = generation_numbers(size, count)
    list_urls = []
    delimeter = '%0A'
    url = ''
    for i in range(len(numbers)):
        url = base_url
        for j in range(len(numbers[i])):
                url += str(numbers[i][j]) + delimeter
        list_urls.append(url)
    return list_urls

urls = create_google_url(size=5, count=2)
driver.get(urls[1])
#print(create_google_url(size=5, count=5))