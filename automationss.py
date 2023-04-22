import string
import random
import time
from bs4 import BeautifulSoup
import ftplib
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 

result = ""
driver = webdriver.Chrome("C:\Internet_Driver\chromedriver.exe") 
driver.get("http://panda1.co.kr/index.php?mid=index&act=dispMemberSignUpForm")

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def name_gen():
    name_list = name_list = ["David", "Jay", "Jenna", "Jenny", "Chrome", "IE", "android", "chemi", "classic", "Colab", "Developer", "vpn", "network", "cancan", "name","sirname"]
    num_list = string.digits[:10]

    return name_list[random.randrange(16)] + num_list[random.randrange(10)] + num_list[random.randrange(10)] + num_list[random.randrange(10)] + num_list[random.randrange(10)]

new_identification = name_gen()
print("ID, PASSWORD: " + new_identification)

driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[1]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[2]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[3]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[4]/div/input').send_keys(new_identification+"@naver.com")
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[5]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[6]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[7]/div/input').send_keys(new_identification+"@gmail.com")
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[9]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[10]/div/input').send_keys(new_identification)
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[8]/div/div/label[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[4]/section/div/form/div[13]/div/input').click()

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/img').click()
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/ul/li[2]/a/img').click()
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[2]/div[3]/div[2]/a').click()

driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/form/table[1]/tbody/tr/td[2]/span/input').send_keys("1일무료체험신청")
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/form/table[2]/tbody/tr[1]/td/ul/li[1]/label').click()
driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/form/table[2]/tbody/tr[2]/td/input').send_keys("없음")

while check_exists_by_xpath("/html/body/div[1]/div[4]/div[2]/form/div[4]/input[2]") == True:
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/form/div[4]/input[2]').click()
    time.sleep(5)

while check_exists_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/div[4]/div/div[2]/div/a") == False:
    time.sleep(30)
    driver.refresh()

data = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div[2]/div[4]/div/div[2]/ul/li[1]/div[2]").text

AA_ID = data.split("\n")[0].split(": ")[1]
AA_PW = "pd82"

time.sleep(2)
driver.get("http://ss.panda1.co.kr")
driver.find_element_by_xpath('/html/body/div[2]/form/div[2]/input').send_keys(AA_ID)
driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/input[1]').send_keys("pd82")
driver.find_element_by_xpath('/html/body/div[2]/form/div[5]/button').click()

while driver.current_url == "http://ss.panda1.co.kr/login":
    time.sleep(30)
    driver.find_element_by_xpath('/html/body/div[2]/form/div[6]/button').click()

result = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div/input').get_attribute("value")
print("SSR INFORMATION ADDRESS: " + result)

r = requests.get(result)
c = r.content
html = str(BeautifulSoup(c, "html.parser"))
file_name = 'vpnprofile'
f = open(file_name, 'w+')
f.write(html)
print("SSR File Loaded")
f.close()

session = ftplib.FTP('jamyong.dothome.co.kr', 'jamyong', 'sw801411')
file = open('vpnprofile', 'rb')
session.storbinary('STOR html/vpnprofile', file)
print("FTP Upload Complete, Please UPDATE Your Subscription Information")
file.close()
session.quit()

print("PROGRAMED FINISHED, CLOSING WEBDRIVER")

driver.quit()