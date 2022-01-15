from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import save_data as sd

def login(driver,url):
    try :
        driver.get(url)
        wait = WebDriverWait(driver,60).until(EC.url_changes(url))
        soup=scrape_page(driver)
        users=sd.save_users(soup.find_all('img'))
        url = driver.current_url
        if (url == "https://www.instagram.com/"):
            #navigate_users(driver)
            navigate_publications(driver)
        else:
            login(driver,url)
    except TimeoutException as ex:
        driver.close()

def scrape_page(driver):
    
    body = driver.execute_script("return document.body")
    source = body.get_attribute('innerHTML') 
    soup = BeautifulSoup(source, "html.parser")
    #get_content(str(soup),driver.title+str(counter))
    return soup
    
    

def get_content (content,file ):
    file = open("./scrappingFiles/"+file+".html","w", encoding='utf-8') 
    file.write(content)
    file.close()

def navigate_users (driver):
    
    try :
        
        soup=scrape_page(driver)
        users=sd.get_users()
        
        for i in range(len(users)):
            url = users[i].profile_url
            driver.get(url)
            wait = WebDriverWait(driver,120).until(EC.url_changes(url))
            soup=scrape_page(driver)
            json_list=soup.find_all("div",{"class":"v1Nh3 kIKUG _bz0w"})
            
            for j in range (len(json_list)):
                code =str(json_list[j].a.attrs['href'])
                sd.save_publication(code,users[i].user_id)
            
    except TimeoutException as ex:
        driver.close()

def navigate_publications(driver):
    try :
        
        soup=scrape_page(driver)
        publications=sd.get_publications()
        
        for i in range(1):#len(publications)):
            url = publications[i].publication_url
            driver.get(url)
            wait = WebDriverWait(driver,120).until(EC.url_changes(url))
            soup=scrape_page(driver)
            
            
            sd.save_comments(soup)
            
    except TimeoutException as ex:
        driver.close()