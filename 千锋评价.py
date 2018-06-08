from selenium import  webdriver
import time,os

url = 'http://stu.1000phone.net/student.php/Public/login'

browser = webdriver.Chrome()
browser.get(url)
id = os.getenv('ID')
pw = '304018'

browser.find_element_by_name('Account').send_keys(id)
browser.find_element_by_name('PassWord').send_keys(pw)
browser.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)

browser.find_element_by_link_text('学员评价').click()
browser.find_element_by_link_text('开始评价').click()
time.sleep(5)

lt = browser.find_elements_by_xpath("//tr[@type='radio']")
for i in lt:
    i.find_element_by_xpath(".//label").click()

ln = browser.find_elements_by_xpath("//tr[@type='textarea']")
for j in ln:
    j.find_element_by_xpath(".//textarea").send_keys('666')

browser.find_element_by_id('addstudent').click()

input('enter: ')
browser.quit()