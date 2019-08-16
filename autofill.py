from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()

driver.get("https://ess.vrl.com.au/")

#login
username = driver.find_element_by_name("sap-alias")
username.clear()
username.send_keys("email")
password = driver.find_element_by_name("sap-password")
password.clear()
password.send_keys("pass")
username.send_keys(Keys.TAB)
username.send_keys(Keys.RETURN)

#unavailability button
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="ul_nav_2"]/li[5]/a')))
unavail_button = driver.find_element_by_xpath('//*[@id="ul_nav_2"]/li[5]/a')
unavail_button.click()

#leave this here just in case, might be useful later
#WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'iFrameId_1565845512836')))
#WebDriverWait(driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//*[@id="iFrameId_1565845940296"]')))

#enter iframe, click new
a = driver.find_elements_by_tag_name("iframe")
#print("***************LIST OF IFRAMES: "+str(a))
driver.switch_to.frame(a[0])
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'WDBC')))
new_button = driver.find_element_by_id('WDBC')
new_button.click()


#FILE READING
f = open("tdb.txt", "r")
startdate = f.readline()
enddate = f.readline()

times = []
temp_times = []

for n in range(0,7):
    temp_times = f.readline().split()
    times.append(temp_times)
    #print(temp_times)

msg = f.readline()
#print(startdate)
#print(enddate)
#print(times)
#print(msg)


#ENTERING
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, 'WDE3')))
startbox = driver.find_element_by_id("WDE3")
startbox.clear()
startbox.send_keys(startdate)

time.sleep(0.3)
endbox = driver.find_element_by_id("WDE7")
endbox.clear()
endbox.send_keys(enddate)

list_boxes = [['WD01AA','WD01F5','WD0242','WD028D'],['WD01B3','WD01FE','WD024B','WD0296'],['WD01BC','WD0207','WD0254','WD029F'],
            ['WD01C5','WD0210','WD025D','WD02A8'],['WD01CE','WD0219','WD0266','WD02B1'],['WD01D7','WD0222','WD026F','WD02BA'],
            ['WD01E0','WD022B','WD0278','WD02C3']]

time.sleep(0.1)
for box in range(len(list_boxes)):
    for slot in range(len(list_boxes[box])):
        current = driver.find_element_by_id(list_boxes[box][slot])
        current.clear()
        current.send_keys(times[box][slot])


msgbox = driver.find_element_by_id("WD02D1")
msgbox.clear()
msgbox.send_keys(msg)


#driver.switch_to.default_content()
#a = driver.find_elements_by_tag_name("iframe")
#print("***************LIST OF IFRAMES: "+str(a))
#driver.switch_to.frame(a[0])
time.sleep(0.1)
submit = driver.find_element_by_id("WD02DA")
submit.click()

