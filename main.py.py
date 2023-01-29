from time import sleep
import random
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
class Crawling():
    def __init__(self, target_url):
        self.driver= uc.Chrome()
        self.target_url = target_url
    def run(self, page):
        linkDetail = []
        link_dictionary = {}
        list_content = []
        # self.driver.get(self.target_url)
        # sleep(random.randint(1,3))
        # self.driver.refresh()
        i = 1
        while True: 
            try: 
                posts = self.driver.find_elements(By.XPATH,"/html/body/div[6]/div/div[1]/div[4]/div/a")
                for ind, postItem in enumerate(posts):
                    href= postItem.get_attribute('href')
                    linkDetail.append(href)
            except Exception as e:
                break
            self.driver.get(self.target_url +str(i))
            i+=1
            if i == page: 
                break
        print(len(linkDetail))
        for link in linkDetail:
            final_list = []
            self.driver.get(link)
            time.sleep(2)
            try: 
                tittle = self.driver.find_element(By.CSS_SELECTOR, 'h1[class="re__pr-title pr-title js__pr-title"]').text
                final_list.append(tittle)
            except:
                final_list.append(None)
            try:
                short_description = self.driver.find_element(By.CSS_SELECTOR,'span[class="re__pr-short-description js__pr-address"]').text
                final_list.append(short_description)
            except:
                final_list.append(None)
    
            table =   self.driver.find_elements(By.CSS_SELECTOR,'div[class="re__pr-specs-content-item"]')
            for i in table: 
                final_list.append(i.text)
            link_dictionary = {'link': link, 'content':final_list }
            list_content.append(link_dictionary)
            with open('your_file2.txt', 'w', encoding='UTF8') as f:
                for line in list_content:
                    f.write(f"{line}\n")
        # return f 
if __name__ == "__main__":
    target_url = r"https://batdongsan.com.vn/nha-dat-cho-thue-tp-hcm/p"
    crawl_obj = Crawling(target_url)
    a= crawl_obj.run(4)
    