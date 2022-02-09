from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement 
from bs4 import BeautifulSoup
import save_data as sd
import time

def login(driver,url):
    try :
        driver.get(url)
        wait = WebDriverWait(driver,60).until(EC.url_changes(url))
        soup=scrape_page(driver)
        #users=sd.save_users(soup.find_all('img'))
        url = driver.current_url
        if (url == "https://www.instagram.com/"):
            navigate_followers(driver,'daniroja6')
            #navigate_users(driver)
            #navigate_publications(driver)
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

def scroll_publications(driver):
    SCROLL_PAUSE_TIME = 0.5
    while True:

        # Get scroll height
        ### This is the difference. Moving this *inside* the loop
        ### means that it checks if scrollTo is still scrolling 
        last_height = driver.execute_script("return document.body.scrollHeight")
        print(last_height)
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:

            # try again (can be removed)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # check if the page height has remained the same
            if new_height == last_height:
                # if so, you are done
                break
            # if not, move on to the next loop
            else:
                last_height = new_height
                continue

def scroll_modal_users(driver):
    scroll = 500
    height=0
    last_height=0
    new_height=10
    count=0
    while True :
        last_height=height
        driver.execute_script("document.querySelector('body > div.RnEpo.Yx5HN > div > div > div > div.isgrP').scrollTop = "+str(scroll))    
        height = int(driver.execute_script("return document.querySelector('body > div.RnEpo.Yx5HN > div > div > div > div.isgrP').scrollTop"))
        new_height = height
        
        if (last_height == new_height):
            count=count+1
        else:
            count=0
        time.sleep(0.5)        
        if( height>=scroll):
            scroll = scroll*height
        
        if(count>2):
            print("end scrolling")
            break;   
    
    

def navigate_followers(driver,original_user):
    try:
        url = driver.current_url
        driver.get(url+original_user+"/" )
        soup=scrape_page(driver)
        element=driver.find_element_by_xpath("//a[@href='/"+original_user+"/following/']")
        element.click()
        time.sleep(3)
        scroll_modal_users(driver)
        users = driver.find_elements_by_xpath("//a[contains(@class, 'notranslate _0imsa')]")
        process_users(users,original_user)
        driver.close()
    except TimeoutException as ex:
        driver.close()
    except NoSuchElementException:
        print("NoSuchElementException")
        driver.close()

def process_users(users, original_user):
    user_id_following=sd.save_or_get_user(original_user)
    
    for user in users:
        user_name = user.get_attribute("title")
        user_id_followed=sd.save_or_get_user(user_name)
        sd.save_relation(user_id_following,user_id_followed)
    print("end saving users and relations")
        

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
    finally:
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