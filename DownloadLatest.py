from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def DownloadLatest(AnimeName, EpNo=1):
        browser = webdriver.Chrome("D:\Python Programs\AnimePahe Scrapper\chromedriver.exe")
        browser.get("https://animepahe.com")

        searchBox = browser.find_element_by_css_selector("#navbarNavDropdown > form > input")
        searchBox.send_keys(AnimeName)

        time.sleep(2)

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
        ##asc = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-bar.row > div.col-6.bar > div > div > label:nth-child(2)")
        ##asc.click()
        ##time.sleep(2)

        try:
                if str(EpNo) in browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(EpNo)+") > div > div.episode-snapshot > a").text:
                        
                        Ep = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(EpNo)+") > div > div.episode-snapshot > a").click()
                else:
                        time.sleep(2)
                        Ep = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(EpNo)+") > div > div.episode-snapshot > a").click()

                time.sleep(3)
                downloadBtn = browser.find_element_by_css_selector("#downloadMenu").click()
                time.sleep(2)
                download = browser.find_element_by_css_selector("#pickDownload > a:nth-child(1)").click()

                time.sleep(5)

                for handle in browser.window_handles:
                        browser.switch_to.window(handle)
                        if 'clearload' in browser.current_url:
                            time.sleep(5)
                            megaBtn = browser.find_element_by_css_selector("#skip_bu2tton").get_attribute("href")
                            browser.get(megaBtn)
                            print(megaBtn)
                            browser.find_element_by_css_selector("#downloadbtn").click()
                            time.sleep(3)
                            browser.get("chrome://Downloads")
                            break;
                        
        except:
                print("No Episode Found")

