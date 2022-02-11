# pip install selenium
# Chrome Driver : https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

#Chrome Driver 버전 업데이트
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

url = 'https://portal.hanyang.ac.kr/sugang/sulg.do'
user_id = ''
user_pw = ''
driver = set_chrome_driver()


#로그인
driver.get(url)
driver.find_element_by_id('btn-user2').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(3)
driver.find_element_by_name('userId').send_keys(user_id)
time.sleep(3)
driver.find_element_by_name('password').send_keys(user_pw)
driver.find_element_by_name('password').send_keys(Keys.RETURN)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])

#이전 희망인원
cur_nums = []
#현재 희망인원
prev_nums = []

#현재 희망인원과 이전 희망인원이 다를때 신청 버튼을 누르도록 함
while(1):
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="snb"]/ul/li[5]/a').click()
    time.sleep(2)

    tbody = driver.find_element_by_xpath('//*[@id="gdMain"]/tbody')
    time.sleep(2)
    rows = tbody.find_elements_by_tag_name('tr')
    time.sleep(2)
    
    for index, value in enumerate(rows):
        body=value.find_elements_by_tag_name("td")[1]
       
        #신청 아직 안된 강의만 cur_nums에 담는다
        if body.find_element_by_id('btn_apply').get_attribute("value") == "신청":
            cur_nums.append(value.find_element_by_id('sincheongInwon').text)
        else:
            break
        
    #cur_nums와 prev_nums의 크기가 다르다는것은 수강 신청이 성공한 강의가 있다는 것.
    #즉, 확인해야할 강의 수가 변경됨 -> prev_nums을 초기화 해주어야 함
    if len(cur_nums) != len(prev_nums):
        for i in range(len(cur_nums)):
            prev_nums.clear()
            prev_nums.append(cur_nums[i])

    #현재 희망인원과 이전 희망인원이 다른지 inspect
    else:
        for i in range(len(cur_nums)):
            if (int)(cur_nums[i]) != (int)(prev_nums[i]):
                rows[i].find_element_by_id('btn_apply').click()
                time.sleep(0.5)
                driver.find_element_by_class_name('ui-button-text').click()
                time.sleep(0.5)
                break

    cur_nums.clear()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="snb"]/ul/li[2]/a').click()
    
    
    #매크로 반복 속도
    time.sleep(5)

    
