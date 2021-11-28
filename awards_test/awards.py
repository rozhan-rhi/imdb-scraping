from bs4 import BeautifulSoup
import requests
from links import Link_Base
from basic import Filter_Base
class Awards(Filter_Base) :
    """it has different methods to find movies' details"""
    
    def __init__(self,url):
        self.url=url
        super().main_page(super().parse_page(self.url))
        
    def awards_page(self):
        self.award_dict={}
        self.page=Link_Base(awards=super().getter_).awards_url
        self.response=super().parse_page(self.page)
        self.all_awards_table=self.response.find("div",id="main").find("div",class_="article listo").find_all("table",class_="awards")
        self.subject_table=[self.each_one for self.each_one in self.response.find("div",id="main").find("div",class_="article listo").find_all("h3") if "event" in self.each_one.a["href"]]
        for self.k,self.v in zip(self.subject_table,self.all_awards_table):
            self.award_key=self.k.text.replace("\n","").strip()
            self.award_value=[self.each_td.text.replace("\n"," ") for self.each_td in self.v.find_all("td",class_="title_award_outcome")]
            self.award_dict[self.award_key]=self.award_value
            
        return self.award_dict
    
       


    
# obj=Awards("https://www.imdb.com/search/title/?genres=crime")
# print(obj.awards_page())