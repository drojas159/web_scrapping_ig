from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import login

base_url = "https://www.instagram.com/"
login_url = "accounts/login/"
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

driver = webdriver.Chrome("./chromedriver/chromedriver.exe", chrome_options=option)
#driver.get("https://www.instagram.com/p/CWeGL2NPaNz/")
#driver.maximize_window()
#time.sleep(10)

login.login(driver,base_url+login_url)
#driver.close()
'''
body = driver.execute_script("return document.body")
source = body.get_attribute('innerHTML') 

soup = BeautifulSoup(source, "html.parser")
data = soup.find('script')
data= str(data)
data=data.replace('<script type="text/javascript">window._sharedData = ','')
data=data.replace(';</script>','')

jasonData=json.loads(str(data))
file1 = open("./scrappingFiles/content1.json","w", encoding='utf-8') 
comments =jasonData['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']
print(len(comments))
for i in range (len(comments)):
    file1.write(comments[i]['node']['text']+"\n")

file1.close()
driver.close()
'''