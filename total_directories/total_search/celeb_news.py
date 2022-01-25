from .t_links import T_Links
import requests
from bs4 import BeautifulSoup
class Celeb_New:
    def find_new(self,celeb_name):
        self.person_news={}
        self.celeb_name=celeb_name
        self.news_url=T_Links().celeb_news_url
        self.req=requests.get(self.news_url)
        self.response=BeautifulSoup(self.req.text,"html.parser")
        self.news_parts=self.response.find("section",id="news-article-list").find_all("article",class_="ipl-zebra-list__item news-article")
        for self.each_part in self.news_parts:
            if self.celeb_name.lower() in self.each_part.a.text.lower():
                self.date=self.each_part.find("ul",class_="news-article__header-detail ipl-inline-list").find("li",class_="ipl-inline-list__item news-article__date").text.replace("\n"," ").strip()
                self.news=self.each_part.find("section",class_="news-article__body").find("div",class_="news-article__content").text.strip()
                break  
        
        try:
            # if self.news!=None:
            self.person_news["date"]=self.date
            self.person_news["news"]=self.news
            return self.person_news
        except:
            return "there is no news about this person"
              
    
obj=Celeb_New()
print(obj.find_new("kim"))