import requests
from bs4 import BeautifulSoup
from ..total_links import Link_Base
from .filter_basic import Filter_Base
class Movie_Storyline(Filter_Base):
    
    def __init__(self,pasre_url,p_link):
        self.pasre_url=pasre_url
        self.p_link=p_link
    
    
    def genre(self):
        self.find_genre=self.pasre_url.find("li",{"data-testid":"storyline-genres"}) #finds genre part
        self.genre_label=self.find_genre.span.text  #finds title(genre)
        self.genre_content=[self.item.a.text for self.item in self.find_genre.find_all("li",role="presentation")]   #finds all genre types of movie
        return self.genre_content
        
        
    def summary(self):
        self.summary_part=self.pasre_url.find("section",{"data-testid":"Storyline"}).find("div",class_="ipc-html-content ipc-html-content--base").div.text
        return [self.summary_part]
    
    
   
    def movie_tag(self):
        self.tag_page=Link_Base(tagline=self.p_link).tagline
        self.parse=super().parse_page(self.tag_page)
        self.tag_part=self.parse.find("div",id="taglines_content")
        self.no_tag=self.tag_part.find("div",id="no_content")
        if self.no_tag==None:
            self.all_tags=self.tag_part.find_all("div",class_="soda")
            self.tag_content=[self.each_tag.text.strip().replace("\n","") for self.each_tag in self.all_tags]
            return self.tag_content
        else:
            return "It looks like we don\'t have any Taglines for this title yet"
        
        
        
    def movie_parents_guide(self):
        self.storyline_dict={}
        self.guide_page=Link_Base(parent_guide=self.p_link).parent_guide
        self.parse=super().parse_page(self.guide_page)
        
        
        def certificate(self):
            self.certification_part=self.parse.find("section",id="certificates")
            self.certificate_label=self.certification_part.find("div",class_="ipl-header__content").h4.text
            self.all_certificates=self.certification_part.find_all("li")
            self.certificate_list=[]
            for self.each_one in self.all_certificates:
                self.certificate_content=self.each_one.a.text.strip().replace("\n","")
                if not self.certificate_content in self.certificate_list:
                    self.certificate_list.append(self.certificate_content)
            self.storyline_dict[self.certificate_label]=self.certificate_list
        certificate(self)
        
        
        def parent_advisor(self):
            self.advice_part=self.parse.find_all("section")
            for self.each_part in self.advice_part:
                self.total_contents=[]
                try:
                    self.advice_label=self.each_part.h4.text
                    if self.advice_label.lower() !="certification" :
                        self.content_parts=self.each_part.find("ul",class_="ipl-zebra-list").find_all("li")
                        for self.each_content in self.content_parts:
                            if self.each_content.find("div",class_="ipl-swapper")==None:
                                self.total_contents.append(self.each_content.text.replace("Edit","").replace("\n","").strip())
                                
                        if not self.advice_label in self.storyline_dict.keys():
                            if not self.total_contents==[] :    
                                self.storyline_dict[ self.advice_label]=self.total_contents
                            else :
                                return f"no {self.advice_label}"
                except:continue
        parent_advisor(self)
        
        return self.storyline_dict

