from bs4 import BeautifulSoup 
from bs4.dammit import EncodingDetector
import requests
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from ..filter_search.movies_based_information.find_movies import Movies
from .t_links import T_Links

class What_To_Watch() :
        
    def parse_page(self,url) :
        """parse the url and save html text"""
        
        self.url=url 
        self.resp=requests.get(self.url)
        self.parse=BeautifulSoup(self.resp.content,"html.parser")
        return self.parse
    
       
    
    def guide(self) :
        self.guid_dict={}
        self.regex="ls([0-9]+)"
        self.page=self.parse_page(T_Links().guide_url)       
        self.watch_guid=[self.item for self.item in self.page.find("div",class_="WatchGuides__ItemWrapper-sc-wu7yfb-1 fCITGH").find_all("div",class_="ipc-slate-card__title-text ipc-slate-card__title-text--clamp-none")]
        self.obj_Movies=Movies()
        for self.each_guid in self.watch_guid : 
            self.guid_label=self.each_guid.text
            self.guide_link=self.each_guid.parent['href']
            self.guid_content=self.obj_Movies.several_movie(T_Links(parent=self.guide_link).second_guide_url)
            self.guid_dict[self.guid_label]=self.guid_content

       
    def watch_parts(self) :
        self.names_list=[]
        
        self.parser = 'html.parser' 
        self.resp = requests.get("http://www.imdb.com/")
        self.http_encoding = self.resp.encoding if 'charset' in self.resp.headers.get('content-type', '').lower() else None
        self.html_encoding = EncodingDetector.find_declared_encoding(self.resp.content, is_html=True)
        self.encoding = self.html_encoding or self.http_encoding
        self.soup = BeautifulSoup(self.resp.content, self.parser, from_encoding=self.encoding)

        #find 2 links 
        self.WTO=[self.link['href'] for self.link in self.soup.find_all('a', href=True)  if "fan-favorites" in self.link['href'].split("/") or "popular" in self.link['href'].split("/") ]
        
        #create complete links
        self.links=["{}{}".format(self.resp.url.replace('com/','com'),self.link) for self.link in self.WTO]

        self.driver=webdriver.Firefox()  
        self.driver.implicitly_wait(20)      
        for self.each_link in self.links :
            self.driver.get(self.each_link)
    
            try :
                #find the name of movies in these 2 links
                self.movie_names=[self.name.text for self.name in self.driver.find_elements(By.CSS_SELECTOR ,'a[class="ipc-poster-card__title ipc-poster-card__title--clamp-2 ipc-poster-card__title--clickable"]')]
                self.names_list.append(self.movie_names)
            
            except :
                continue            
        self.driver.close()
        
        #creating namedtuple of tabs and movie_names
        (self.tabs , self.movie_names )=["fan_favoratis","most_popular"] , self.names_list
        self.WTW=namedtuple("WTW",self.tabs)
        self.obj_=self.WTW(*self.movie_names)
        return self.obj_._asdict()




