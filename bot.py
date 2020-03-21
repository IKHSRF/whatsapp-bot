from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

input("press key after qr code")
time.sleep(5)

names = ["Rausan"]

for name in names:

    person = driver.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name))
    person.click()

    for i in range(1, 3):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_css_selector(
        "span._F7Vk.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]

    if msg[-1] == "Tes bot python":
        reply = driver.find_elements_by_class_name(
            "_3u328.copyable-text.selectable-text")

        reply[1].clear()
        reply[1].send_keys("ini tes ke 12")
        reply[1].send_keys(Keys.RETURN)
    else:
        reply = driver.find_elements_by_class_name(
            "_3u328.copyable-text.selectable-text")

        reply[1].clear()
        reply[1].send_keys("ini tes ke 13")
        reply[1].send_keys(Keys.RETURN)
