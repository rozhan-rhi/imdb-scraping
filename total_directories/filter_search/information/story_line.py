import requests
from bs4 import BeautifulSoup
from ..total_links import Link_Base
from .filter_basic import Filter_Base
import re

class Movie_Storyline(Filter_Base):
    
    def __init__(self,parse_url,p_link):
        self.parse_url=parse_url
        self.p_link=p_link
    
    
    def genre(self):
        self.genre_content=[self.item.text for self.item in self.parse_url.find_all("a",href=True) if "search" in self.item['href'].split("/") and "?genres" in re.split('/|=',self.item['href'])]   #finds all genre types of movie
        return self.genre_content
        
        
    def summary(self):
        try :
            self.summary_part=self.parse_url.find("section",{"data-testid":"Storyline"}).find("div",class_="ipc-html-content ipc-html-content--base").div.text.strip()
            return [self.summary_part]
        except :pass
    
   
    def movie_tag(self):
        try :
            self.link_tag=[self.each['href'] for self.each in self.parse_url.find_all("a",href=True) if "taglines" in re.split("/|?" , self.each['href'] )]
            print(self.link_tag)
                # self.line_names=["odd","even"]
                # for self.each_line_name in self.line_names :
                #     self.tagline_page=[self.tagline.text for self.tagline in self.parse_page(f"{'https://www.imdb.com'}{''.join(self.link_tag)}").find_all("div",class_=f"soda {self.each_line_name}")]
                #     print(self.tagline_page)
                # self.tagline_page2=self.parse_url.find("span",class_="ipc-metadata-list-item__list-content-item").text 
                # return self.tagline_page2

        except:pass
            
            
        
        # self.tag_link=Link_Base(tagline=self.p_link).tagline
        # self.parse=super().parse_page(self.tag_link)
        # self.tag_part=self.parse.find("div",id="taglines_content")
        # try :
        #     self.all_tags=self.tag_part.find_all("div")
        #     self.tag_content=[self.each_tag.text.strip().replace("\n","") for self.each_tag in self.all_tags]
        # except :
        #     self.tag_content="no tagline"
        # finally :
        #     return self.tag_content
        
        
    def movie_parents_guide(self):
        self.storyline_dict={}
        self.guide_link=Link_Base(parent_guide=self.p_link).parent_guide
        self.parse=super().parse_page(self.guide_link)
        
        def certificate(self):
            # self.certification_part=self.driver.find_element_by_class_name("ipl-zebra-list__label")
            self.certificate_label=self.parse.find("div",class_="ipl-header__content").text
            self.all_certificates=[self.each_ct.text for self.each_ct in self.parse.find_all("a",href=True) if "certificates" in re.split("?|=" , self.each_ct)]
            # self.certificate_list=[]
            # for self.each_one in self.all_certificates:
            #     self.certificate_content=self.each_one.a.text.strip().replace("\n","")
            #     if not self.certificate_content in self.certificate_list:
            #         self.certificate_list.append(self.certificate_content)
            self.storyline_dict[self.certificate_label]=self.all_certificates
                # self.certificate_list
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
                            else:
                                self.storyline_dict[ self.advice_label]="no information"
                           
                except:continue
        # parent_advisor(self)
        
        return self.storyline_dict