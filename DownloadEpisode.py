from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import pyperclip as pp


def Download(AnimeName, EpNo):
##        opts = ChromeOptions()
##        opts.add_experimental_option("detach", True)
##        browser = Chrome(chrome_options=opts)
        browser = webdriver.Chrome("chromedriver.exe")
        browser.get("https://animepahe.com")

        searchBox = browser.find_element_by_css_selector("#navbarNavDropdown > form > input")
        searchBox.send_keys(AnimeName)

        dropBox = browser.find_element_by_css_selector("#navbarNavDropdown > form > div")

        time.sleep(3)

        index = 1
        while True:
                print("Before: ", index)
                try:
                        if 'TV' in browser.find_element_by_css_selector("#navbarNavDropdown > form > div > ul > li:nth-child("+str(index)+") > a > div.result-status").text and AnimeName.replace(" ", "").lower() in browser.find_element_by_css_selector("#navbarNavDropdown > form > div > ul > li:nth-child("+str(index)+") > a > div.result-title").text.replace(" ","").lower():
                                browser.find_element_by_css_selector("#navbarNavDropdown > form > div > ul > li:nth-child("+str(index)+") > a").click() #link can be obtained by .get_attribute("href")
                                break
                        else:
                                index+=1
                        print("After:" , index)
                except:
                        break
                        print("Excepted")
                        
        asc = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-bar.row > div.col-6.bar > div > div > label:nth-child(2)")
        asc.click()
        time.sleep(4)

        index2 = 1
        try:
                while True:
                        if str(EpNo) in browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(index2)+") > div > div.episode-snapshot > a").text:
                                Ep = browser.find_element_by_css_selector("body > section > article > div.content-wrapper > div.episode-list-wrapper > div > div:nth-child("+str(index2)+") > div > div.episode-snapshot > a").click()
                                break;
                                time.sleep(2)
                        index2+=1
                        
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
                            link = browser.find_element_by_css_selector("#url").get_attribute("href")
                            break
                        
        except:
                print("No Episode Found")

#Download(sys.argv[1], sys.argv[2])
