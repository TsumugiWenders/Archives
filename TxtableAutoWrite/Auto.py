import time
import datetime
import random
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
#from openpyxl import Workbook
#from openpyxl.utils import get_column_letter
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

today_time=str(datetime.datetime.now().year)+"/"+str(datetime.datetime.now().month)+"/"+str(datetime.datetime.now().day)

url=""#将健康表的地址copy过来就行。
driver = Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get(url)

#AutoPlanA
#time.sleep(20)
#driver.find_element_by_id('header-login-btn').click()
#time.sleep(2)
#driver.switch_to_frame(driver.find_element_by_id('login_frame'))
#driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#driver.find_element_by_xpath('//*[@id="u"]').send_keys('')
#driver.find_element_by_xpath('//*[@id="p"]').send_keys('')
#driver.find_element_by_xpath('//*[@id="login_button"]').click()

#AutoPalnB
driver.find_element_by_class_name('unlogin-container').click()#点击登入按钮
time.sleep(1)
driver.switch_to.frame(driver.find_element_by_id('login_frame'))
driver.find_element_by_class_name('img_out_focus').click()
#登入账号,用快速登入的功能,前提,已经电脑qq登入了
driver.switch_to.parent_frame()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="canvasContainer"]/div[1]/div[2]').click()
time.sleep(0.5)

#ByHand
print("****** Import Hint 重要提示******")
print("Please make sure you have completed manual login before you execute.")
print("在您执行之前请确认已经完成手工登录")
print("*********************************")
input("Press ENTER to conitnue or Crtl+C to exit.")

############
#自动填写部分#
############

def randomtemp():
    temp = random.uniform(36.0, 36.9)
    lstemp = str(temp)
    endtemp = lstemp[0:4]
    return endtemp

def res():
    return random.choice(['宿舍-食堂', '宿舍-食堂-图书馆', '宿舍-食堂-教室', '宿舍-食堂-教室-图书馆', ])

def persion():
    #自动体温
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(randomtemp())
    ActionChains(driver).key_down(Keys.TAB).perform()
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(randomtemp())
    ActionChains(driver).key_down(Keys.TAB).perform()
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(randomtemp())
    #新定位
    ActionChains(driver).key_down(Keys.TAB).perform()
    ActionChains(driver).key_down(Keys.TAB).perform()
    #自动轨迹
    driver.find_element_by_id('alloy-simple-text-editor').click()
    driver.find_element_by_id('alloy-simple-text-editor').send_keys(res())
    pass

def nullpersion():
    ActionChains(driver).key_down(Keys.TAB).perform()
    ActionChains(driver).key_down(Keys.TAB).perform()
    ActionChains(driver).key_down(Keys.TAB).perform()
    ActionChains(driver).key_down(Keys.TAB).perform()
    changerow()
    pass

def changerow():
    ActionChains(driver).key_down(Keys.ENTER).perform()
    for i in range(0,4):
        ActionChains(driver).key_down(Keys.LEFT).perform()
        pass
    pass

#开始定位

for i in range(0, 2):#这里的循环的次数，修改为自己的信息所在的行号。
    ActionChains(driver).key_down(Keys.ENTER).perform()
    #driver.find_element_by_id('alloy-simple-text-editor').send_keys(Keys.ENTER)

for i in range(0,5):
    ActionChains(driver).key_down(Keys.TAB).perform()

#序号=i++
for i in range(0,39):

    if i==31:
        nullpersion()
        pass

    persion()
    changerow()
