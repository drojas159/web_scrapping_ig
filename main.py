from selenium import webdriver
from bs4 import BeautifulSoup
import time
import navigate
import sys
sys.path.append('c:\\workarea\\web_scrapping_ig\\model')
sys.path.append('c:\\workarea\\web_scrapping_ig\\persistence')

print(sys.path)

base_url = "https://www.instagram.com/"
login_url = "accounts/login/"
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
users={}

driver = webdriver.Chrome("./chromedriver/chromedriver.exe", chrome_options=option)
#driver.get("https://www.instagram.com/p/CWeGL2NPaNz/")
#driver.maximize_window()
#time.sleep(10)

navigate.login(driver,base_url+login_url)
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