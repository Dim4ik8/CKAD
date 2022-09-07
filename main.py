from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime

email = 'dmitry.zhlobo@yandex.ru'
phone = '+7 9653972579'
url = 'https://pays.avtodor-tr.ru/ckad/payment-of-debt/'
driver = webdriver.Chrome()


def main():
    driver.get(url=url)


    grz_input = driver.find_elements(By.CSS_SELECTOR, 'input')[2]
    grz_input.send_keys('А 777 АА 777')

    phone_input = driver.find_elements(By.CSS_SELECTOR, 'input')[3]
    phone_input.send_keys(phone)

    # sms_code_button = driver.find_elements(By.CSS_SELECTOR, 'button')[1]
    # sms_code_button.click()

    email_input = driver.find_elements(By.CSS_SELECTOR, 'input')[4]
    email_input.send_keys(email)
    check_button = driver.find_elements(By.CSS_SELECTOR, 'button')[1]
    check_button.click()
    time.sleep(2)
    check_button1 = driver.find_elements(By.CSS_SELECTOR, 'button')[2]
    check_button1.click()
    time.sleep(5)

    with open('numbers.txt', 'r', encoding='UTF-8') as f:
        numbers_data = f.readlines()

    for number in numbers_data:
        time.sleep(2)
        grz_input = driver.find_elements(By.CSS_SELECTOR, 'input')[2]
        grz_input.send_keys(number)
        time.sleep(2)

        check_button = driver.find_elements(By.CSS_SELECTOR, 'button')[1]
        check_button.click()
        time.sleep(2)

        result_element = driver.find_elements(By.CSS_SELECTOR, '.form-step')[3]
        result = result_element.text

        if 'Задолженность отсутствует' in result:
            next_button = driver.find_elements(By.CSS_SELECTOR, 'button')[2]
            next_button.click()
        else:
            with open('output.txt', 'a', encoding='UTF-8') as f:
                f.write(number + result + '\n\n#######################################\n\n')
            next_button = driver.find_elements(By.CSS_SELECTOR, 'button')[2]
            next_button.click()

    with open('output.txt', 'a', encoding='UTF-8') as f:
        f.write('Работа программы завершена корректно, все авто проверены! ')

    driver.quit()


if __name__ == '__main__':
    main()
