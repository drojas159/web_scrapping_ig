from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import save_users as su

counter = 0

def login(driver,url):
    
    print(url)
    
    print(driver.title)
    try :
        driver.get(url)
        wait = WebDriverWait(driver,60).until(EC.url_changes(url))
        scrape_page(driver)
        url = driver.current_url
        if (url == "https://www.instagram.com/"):
            navigate(driver)
        else:
            login(driver,url)
    except TimeoutException as ex:
        driver.close()

def scrape_page(driver):
    global counter
    counter += 1
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML') 
    soup = BeautifulSoup(source, "html.parser")
    get_html(str(soup.find_all('img')),driver.title+str(counter))
    su.save_users(soup.find_all('img'))
    
    

def get_html (content,file ):
    file = open("./scrappingFiles/"+file+".txt","w", encoding='utf-8') 
    file.write(content)
    file.close()

def navigate (driver):
    print ("hola")
    ##driver.close()