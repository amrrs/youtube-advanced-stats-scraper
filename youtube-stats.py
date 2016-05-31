import time
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

#colnames = ['Link','URL','link1','link2']
#input csv file with video urls 
inpdata = pd.read_csv('input.csv',header=0,encoding = 'iso-8859-1')
url_list = inpdata.URL.tolist()
#url_list = ['https://www.youtube.com/watch?v=DSEun41_6PQ']

i = 0
for url in url_list:
    print(url)
#creating output csv file
with open('output.csv', 'w',newline='') as csvfile:
    autowriter = csv.writer(csvfile)
    autowriter.writerow(['URL','Shares','Subs','Avg Time'])

    browser = webdriver.Chrome()

#change your channel url here

    #url_list = ["https://www.youtube.com/watch?v=lzlfDjk4qHw",'https://www.youtube.com/watch?v=2xffwSSC7VM']

    for url in url_list:
        i = i + 1 #just a progress counter
        browser.get(url)
        time.sleep(1)

        elem = browser.find_element_by_tag_name("body")

        try:
            time.sleep(1)
            browser.find_element_by_class_name("yt-uix-menu-trigger").click()
            time.sleep(1)
            browser.find_element_by_class_name('action-panel-trigger-stats').click()
            time.sleep(1)
            shares = browser.find_element_by_xpath('//*[@id="watch-actions-stats"]/table/tbody/tr/td[4]/div').text
            subs = browser.find_element_by_xpath('//*[@id="watch-actions-stats"]/table/tbody/tr/td[3]/div').text
            shares = int(shares.replace(',', ''))
            subs = int(subs.replace(',', ''))
            browser.find_element_by_class_name('stats-bragbar-watch-time').click()
            time.sleep(1)
            avg_time = browser.find_element_by_xpath('//*[@id="stats-chart-tab-watch-time"]/span/span[2]').text
            #except NoSuchElementException:
        except:
            shares = 'NA'
            subs = 'NA'
            avg_time = 'NA'
            pass
        print(str(i))
        autowriter.writerow([browser.current_url,shares,subs,avg_time])



