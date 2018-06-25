from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Download(AnimeName, EpNo):
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get("https://animepahe.com")

        searchBox = browser.find_element_by_css_selector("#navbarNavDropdown > form > input")
        searchBox.send_keys(AnimeName)

        dropBox = browser.find_element_by_css_selector("#navbarNavDropdown > form > div")

        time.sleep(3)

        index = 1
        while True:
                try:
                        if 'TV' in browser.find_element_by_css_selector("#navbarNavDropdown > form > div > ul > li:nth-child("+str(index)+") > a > div.result-status").text and AnimeName.replace(" ", "").lower() in browser.find_element_by_css_selector("#navbarNavDropdown > form > div > ul > li:nth-child("+str(index)+") > a > div.result-title").text.replace(" ","").lower():
                                browser.find_element_by_css_selector("#navbarNavDropdown > form > div > ul > li:nth-child("+str(index)+") > a").click() #link can be obtained by .get_attribute("href")
                                break
                        else:
                                index+=1
                except:
                        break
                        print("Excepted")
                        
        asc = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-bar.row > div.col-6.bar > div > div > label:nth-child(2)")
        asc.click()
        time.sleep(4)

        con1 = True
        while con1:
                index2 = 1
                try:
                        addressCheck=''
                        con2 = True
                        while con2:
                                if str(EpNo) in browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(index2)+") > div > div.episode-snapshot > a").text:
                                        Ep = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(index2)+") > div > div.episode-snapshot > a")
                                        addressCheck = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(index2)+") > div > div.episode-snapshot > a").get_attribute("href")
                                        Ep.send_keys(Keys.CONTROL + Keys.RETURN)
                                        con2 = False
                                        break
                                        print(index2)
                                        time.sleep(2)
                                else:
                                        index2+=1

                        
                        for handle in browser.window_handles:
                                browser.switch_to.window(handle)
                                if "play" in browser.current_url:
                                        time.sleep(3)
                                        downloadBtn = browser.find_element_by_css_selector("#downloadMenu").click()
                                        time.sleep(2)
                                        downloadBtn = browser.find_element_by_css_selector("#downloadMenu").click()
                                        download = browser.find_element_by_css_selector("#pickDownload > a:nth-child(1)").get_attribute("href")
                                        browser.get(download)
                                        

                        time.sleep(5)
                        for handle in browser.window_handles:
                                browser.switch_to.window(handle)
                                if 'clearload' in browser.current_url:
                                        time.sleep(5)
                                        megaBtn = browser.find_element_by_css_selector("#skip_bu2tton").get_attribute("href")
                                        browser.get(megaBtn)
                                        browser.find_element_by_css_selector("#downloadbtn").click()
                                        time.sleep(5)
                                        browser.get("chrome://downloads/")
                                        EpNo+=1

                        for handle in browser.window_handles:
                                browser.switch_to.window(handle)
                                if 'animepahe' in browser.current_url:
                                        print("This one")
                                
                except:
                        print("No Episode Found")
                        if "animepahe" not in browser.current_url:
                                browser.close()
                                browser.switch_to.window(browser.window_handles[0])
                        else:
                                con1 = False
                                break
                        con2 = False

Download("Fumikiri Jikan", 10)
