import requests
from bs4 import BeautifulSoup
from links import Link_Base


class Filter_Base :
    """it has different methods to find movies' details"""

    def __str__(self):
        return f"the result of Filter_Base class is :\n{self.movie_specs}"

    def parse_page(self,url) :
        """parse the url and save html text"""
        self.url=url
        self.response_=requests.get(self.url)
        self.parse=BeautifulSoup(self.response_.text,"html.parser")
        return self.parse
    
   

    def main_page(self,html_text) :
        """finds personal link of movie then goes to movie page and parses it"""
        self.movie_content=html_text
        self.personal_link=self.movie_content.h3.a["href"] #finds special url of movie
        self.new_page_movie=Link_Base(personal_link=self.personal_link).main_page_url #goes to movie page
        self.req_new_page=requests.get(self.new_page_movie)
        self.parse_new_page=BeautifulSoup(self.req_new_page.text,"html.parser")
        return self.parse_new_page


    def movie_name(self,parse_text):
        self.finding_name=parse_text
        self.name=self.finding_name.h3.a.text #finds the name of movie
        return self.name
        

    def movie_detail(self,page) :
        """finds all information about movie"""
        self.movie_specs={}  #save all movies with their details        
        self.page=page


        def genre(self):
            self.find_genre=self.page.find("li",{"data-testid":"storyline-genres"}) #finds genre part
            self.genre_label=self.find_genre.span.text  #finds title(genre)
            self.genre_content=[self.item.a.text for self.item in self.find_genre.find_all("li",role="presentation")]   #finds all genre types of movie
            self.movie_specs[self.genre_label]=self.genre_content
        genre(self)


        def runtime(self) :
            try:
                #finds runtime part
                self.runtime_part=self.page.find("section",{"data-testid":"TechSpecs"}).find("li",{"data-testid":"title-techspec_runtime"})   
                self.runtime_label=self.runtime_part.find("span",class_="ipc-metadata-list-item__label").text   #finds the title
                #finds the time of movie
                self.runtime_content=self.runtime_part.find("div",class_="ipc-metadata-list-item__content-container")
                if self.runtime_content.find("span",class_="ipc-metadata-list-item__list-content-item"):
                    self.time_movie=self.runtime_content.find("span",class_="ipc-metadata-list-item__list-content-item").text 
                else:
                    self.time_movie=self.runtime_content.text
                self.movie_specs[self.runtime_label]=self.time_movie
            except:pass
        runtime(self)


        def rating(self) :        
            try:
                #finds the rate of movie
                self.rating_part=self.page.find("div",class_="RatingBar__ButtonContainer-sc-85l9wd-1 idYUsR").find("div",class_="AggregateRatingButton__ContentWrap-sc-1ll29m0-0").span.text  
                self.movie_specs["rating"]=self.rating_part
            except:
                pass
        rating(self)


        def extra(self):
            #finds more information about movie
            self.extra_details=self.page.find("section",{"data-testid":"Details"}).find("div",{"data-testid":"title-details-section"})  
            self.detail_parts=self.extra_details.find_all("li",class_="ipc-metadata-list__item") #finds all details parts
            for self.each_part in self.detail_parts:
                try: #this try/except finds labels of parts except IMDBPro.some labels are in "a" tag and some in "span" tag
                    self.part_label=self.each_part.find("span",class_="ipc-metadata-list-item__label").text
                except:
                    if not "companycredits" in self.each_part["data-testid"]:
                        self.part_label=self.each_part.find("a",class_="ipc-metadata-list-item__label ipc-metadata-list-item__label--link").text
                

                self.find_content=self.each_part.find("div",class_="ipc-metadata-list-item__content-container") #finds the content part of movie
                try :#this try/except finds the content of parts.some contents are in "a" tag and some in "span" tag
                    if self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item") : 
                        self.part_content=[self.each_one.text for self.each_one in  self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item")]

                    else :
                        self.part_content=[self.each_one.text for self.each_one in self.find_content.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
                except:
                    continue
                self.movie_specs[self.part_label]=self.part_content
        extra(self)

            

        def people(self):
            try: #this part finds the name of the humans in basic parts
                self.human_info=self.page.find("div",class_="Hero__ContentContainer-kvkd64-10") #finds human table
                self.find_information=self.human_info.find("div",class_="PrincipalCredits__PrincipalCreditsPanelWideScreen-hdn81t-0 iGxbgr") #one step closer
                self.info_parts=self.find_information.find_all("li",class_="ipc-metadata-list__item") #finds different parts of human table
                for self.each_one in self.info_parts:
                    if self.each_one.find("span",class_="ipc-metadata-list-item__label")==None: #this if/else for finding label of each part
                        self.label_info=self.each_one.find("a",class_="ipc-metadata-list-item__label ipc-metadata-list-item__label--link").text
                    else:
                        self.label_info=self.each_one.find("span",class_="ipc-metadata-list-item__label").text 

                    if self.label_info.lower()=="stars":
                        self.star_link=(self.each_one.find("a",class_="ipc-metadata-list-item__icon-link"))["href"]
                        self.all_actor_link=f"https://www.imdb.com{self.star_link}"
                        self.actor_page=self.parse_page(self.all_actor_link)
                        self.actors_table=self.actor_page.find("table",class_="cast_list").find_all("tr")
                        self.actors_names=[]
                        for self.each_table in self.actors_table:
                            try:
                                self.delete_option=self.each_table.find("td",class_="primary_photo")
                                self.all_options=self.each_table.find_all("td")
                                for self.each_option in self.all_options:
                                    if "name" in self.each_option.a["href"] :
                                        if self.each_option!=self.delete_option:
                                            self.name=self.each_option.a.text
                                            self.actors_names.append(self.name.strip().replace("\n",""))
                         
                            except:pass
                        self.movie_specs["actors"]=self.actors_names
                     

                    else:
                        #finds the content of each part
                        self.content_info=[self.item.text for self.item in self.each_one.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
                        self.movie_specs[self.label_info]=self.content_info
            except:pass
        people(self)
        return self.movie_specs
