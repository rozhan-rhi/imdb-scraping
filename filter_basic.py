import requests
from bs4 import BeautifulSoup
from links import Link_Base


class Filter_Base :
    """it has different methods to find movies' details"""
    movie_specs={}  #save all movies with their details

    def __str__(self):
        return f"the result of Filter_Base class is :\n{Filter_Base.movie_specs}"

    def parse_page(self,url) :
        """parse the url and save html text"""
        self.url=url
        self.req=requests.get(self.url)
        self.parse=BeautifulSoup(self.req.text,"html.parser")
        return self.parse
    
   

    def main_page(self,parse_func) :
        """finds personal link of movie then goes to movie page and parses it
        put parse_page as parse_func argument"""
        self.movie_content=parse_func
        self.movie_name=self.movie_content.h3.a.text #finds the name of movie
        Filter_Base.movie_specs[self.movie_name]={} 
        self.personal_link=self.movie_content.h3.a["href"] #finds special url of movie
        self.new_page_movie=Link_Base(personal_link=self.personal_link).main_page_url #goes to movie page
        self.req_new_page=requests.get(self.new_page_movie)
        self.parse_new_page=BeautifulSoup(self.req_new_page.text,"html.parser")
        return self.parse_new_page
        

    def movie_detail(self,func_page) :
        """finds all information about movie
        put main_page as func_page argument"""
        self.page=func_page
        self.find_genre=self.page.find("li",{"data-testid":"storyline-genres"}) #finds genre part
        self.genre_label=self.find_genre.span.text  #finds title(genre)
        self.genre_content=[self.item.a.text for self.item in self.find_genre.find_all("li",role="presentation")]   #finds all genre types of movie
        Filter_Base.movie_specs[self.movie_name][self.genre_label]=self.genre_content


        try:
            #finds runtime part
            self.runtime_part=self.page.find("section",{"data-testid":"TechSpecs"}).find("li",{"data-testid":"title-techspec_runtime"})   
            self.runtime_label=self.runtime_part.find("span",class_="ipc-metadata-list-item__label").text   #finds the title
            #finds the time of movie
            self.runtime_content=self.runtime_part.find("div",class_="ipc-metadata-list-item__content-container").find("span",class_="ipc-metadata-list-item__list-content-item").text 
            Filter_Base.movie_specs[self.movie_name][self.runtime_label]=self.runtime_content
        except:pass
        try:
            #finds the rate of movie
            self.rating_part=self.page.find("div",class_="RatingBar__ButtonContainer-sc-85l9wd-1 idYUsR").find("div",class_="AggregateRatingButton__ContentWrap-sc-1ll29m0-0").span.text  
            Filter_Base.movie_specs[self.movie_name]["rating"]=self.rating_part
        except:
            pass

        #finds more information about movie
        self.extra_details=self.page.find("section",{"data-testid":"Details"}).find("div",{"data-testid":"title-details-section"})  
        self.detail_parts=self.extra_details.find_all("li",class_="ipc-metadata-list__item") #finds all details parts
        for self.each_part in self.detail_parts:
            try: #this try/except finds labels of parts except IMDBPro.some labels are in "a" tag and some in "span" tag
                self.part_label=self.each_part.find("span",class_="ipc-metadata-list-item__label").text
            except:
                if not "companycredits" in self.each_part["data-testid"]:
                    self.part_label=self.each_part.find("a",class_="ipc-metadata-list-item__label").text
            

            self.find_content=self.each_part.find("div",class_="ipc-metadata-list-item__content-container") #finds the content part of movie
            try :#this try/except finds the content of parts.some contents are in "a" tag and some in "span" tag
                if self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item") : 
                    self.part_content=[self.each_one.text for self.each_one in  self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item")]

                else :
                    self.part_content=[self.each_one.text for self.each_one in self.find_content.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
            except:
                continue
            Filter_Base.movie_specs[self.movie_name][self.part_label]=self.part_content
        
       
        try: #this part finds the name of the humans in basic parts
            self.human_info=self.page.find("div",class_="Hero__ContentContainer-kvkd64-10") #finds human table
            self.find_information=self.human_info.find("div",class_="PrincipalCredits__PrincipalCreditsPanelWideScreen-hdn81t-0 iGxbgr") #one step closer
            self.info_parts=self.find_information.find_all("li",class_="ipc-metadata-list__item") #finds different parts of human table
            for self.each_one in self.info_parts:
                if self.each_one.find("span",class_="ipc-metadata-list-item__label")==None: #this if/else for finding label of each part
                    self.label_info=self.each_one.find("a",class_="ipc-metadata-list-item__label ipc-metadata-list-item__label--link").text
                else:
                    self.label_info=self.each_one.find("span",class_="ipc-metadata-list-item__label").text 
                #finds the content of each part
                self.content_info=[self.item.text for self.item in self.each_one.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
                Filter_Base.movie_specs[self.movie_name][self.label_info]=self.content_info
        except:pass
        return  Filter_Base.movie_specs