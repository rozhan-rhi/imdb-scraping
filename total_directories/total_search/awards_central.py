import requests 
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector, encoding_res
import re


class Central :
    
    def parse_page(self,url) :
        self.url=url
        self.response_=requests.get(self.url)
        self.http_encoding=self.response_.encoding if "charset" in self.response_.headers.get('content-type','').lower() else None
        self.html_encoding=EncodingDetector.find_declared_encoding(self.response_.content, is_html=True)
        self.encoding=self.http_encoding or self.html_encoding
        self.soup=BeautifulSoup(self.response_.text, "html.parser")
        return self.soup
        
    def center(self) :
        self.WN_dict={}
        self.base_url="https://www.imdb.com/search/title/"
        self.search_page=self.parse_page(self.base_url)
        self.title_groups=[self.each_label.parent for self.each_label in self.search_page.find_all("div",class_="label") if self.each_label.h3.text.lower()=="title groups"]
        for self.parent_group in self.title_groups :
            self.win_nom=[self.each_group.text.strip().lower().replace("winning","winner").replace("nominated","nominee") for self.each_group in self.parent_group.find_all("td") if "Winning" in self.each_group.text.split("-") or "Nominated" in self.each_group.text.split("-")]
        
        for self.name_group in self.win_nom :
            self.name_group=re.split("-| ",self.name_group)
            if "award" in self.name_group :
                self.name_group.remove("award")
            elif "best" in self.name_group and "nominee" in self.name_group :
                self.name_group.insert(0,"oscar")
                
            self.regex="tt([0-9]+)"
            self.link_group=f"https://www.imdb.com/search/title/?groups={'_'.join(self.name_group).replace('nominee','nominees')}"
            self.movie_group=[self.movie_name.text.strip().replace("X","") for self.movie_name in self.parse_page(self.link_group).find_all("a",href=True) if re.findall("tt([0-9]+)",self.movie_name['href'])]
            self.movie_group=list(filter(None,self.movie_group))
            self.WN_dict[' '.join(self.name_group)]=self.movie_group
        return self.WN_dict



