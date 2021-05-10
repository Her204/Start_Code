import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 

options = Options()
options.headless=True

def Get_info():
    url = input('Enter Youtube Video Url- ')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    Vid={}
    References = {}

    References['Title'] = "//*[@id='container']/h1"
    References['Channel'] = "//*[@id='text']/a"
    References['Subscribers'] = "//*[@id='owner-sub-count']"
    References['Tags'] = "//*[@id='container']/yt-formatted-string"
    References['Views'] = "//*[@id='count']/yt-view-count-renderer"
    References['Likes'] = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-formatted-string"
    References['Dislikes'] = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string"
    References['Dislikes'] = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[7]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[2]/a/yt-formatted-string"
    References['DateUpload']= "//*[@id='date']/yt-formatted-string"

    INFO_List = list()
    for i in range(0,len(References)):
        driver_elements = driver.find_element_by_xpath(References[list(References.keys())[i]])
        INFO_List.append(driver_elements.text)
    Vid = dict(zip(list(References.keys()), INFO_List))
    Vid['Link'] = url
    Related = {}
    Related_video_links = []
    Related_video_title = []
    Related_videos = driver.find_elements_by_xpath("//*[@id='video-title']")
    Related_video_links = [links.get_attribute("href") for links in driver.find_elements_by_xpath("//*[@id='dismissable']/div/div[1]/a")]
    Related_video_title = [videos.text for videos in Related_videos][:len(Related_video_links)]
    Related = dict(zip(Related_video_title, Related_video_links))
    Vid['Related'] = Related
    with open('vfile.json', 'w', encoding='utf8') as ou:
        json.dump(Vid, ou, ensure_ascii=False)
    return(Vid)
Get_info()