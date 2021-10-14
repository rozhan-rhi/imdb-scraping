import requests
from bs4 import BeautifulSoup
from links import Link_Base


class Filter_Base :
    movie_specs={}

    def parse_page(self,url) :
        self.url=url
        self.req=requests.get(self.url)
        self.parse=BeautifulSoup(self.req.text,"html.parser")

    
    
    def several_movie(self,func1,func2):
        self.list_movies=self.parse.find_all("div",class_="lister-item mode-advanced")
        for self.each_movie in self.list_movies :
            self.movie_content=self.each_movie.find("div",class_="lister-item-content")
            self.total_content=func2(func1(self.movie_content))
        return  self.total_content


    def one_movie(self,func1,func2):
        self.movie=self.parse.find("div",class_="lister-item mode-advanced")
        self.movie_content=self.movie.find("div",class_="lister-item-content")
        self.total_content=func2(func1(self.movie_content))
        return  self.total_content
    
    def main_page(self,html_content) :
        self.movie_content=html_content
        self.movie_name=self.movie_content.h3.a.text 
        Filter_Base.movie_specs[self.movie_name]={}
        self.personal_link=self.movie_content.h3.a["href"]
        self.new_page_movie=Link_Base(personal_link=self.personal_link).main_page_url
        self.req_new_page=requests.get(self.new_page_movie)
        self.parse_new_page=BeautifulSoup(self.req_new_page.text,"html.parser")
        return self.parse_new_page



    def movie_detail(self,page) :
        self.page=page
        self.find_genre=self.page.find("li",{"data-testid":"storyline-genres"})
        self.genre_label=self.find_genre.span.text
        self.genre_content=[self.item.a.text for self.item in self.find_genre.find_all("li",role="presentation")]
        Filter_Base.movie_specs[self.movie_name][self.genre_label]=self.genre_content


        try:
            self.runtime_part=self.parse_link.find("section",{"data-testid":"TechSpecs"}).find("li",{"data-testid":"title-techspec_runtime"})
            self.runtime_label=self.runtime_part.find("span",class_="ipc-metadata-list-item__label").text
            self.runtime_content=self.runtime_part.find("div",class_="ipc-metadata-list-item__content-container").find("span",class_="ipc-metadata-list-item__list-content-item").text
            Filter_Base.movie_specs[self.movie_name][self.runtime_label]=self.runtime_content
        except:pass
        try:
            self.rating_part=self.parse_link.find("div",class_="RatingBar__ButtonContainer-sc-85l9wd-1 idYUsR").find("div",class_="AggregateRatingButton__ContentWrap-sc-1ll29m0-0").span.text
            Filter_Base.movie_specs[self.movie_name]["rating"]=self.rating_part
        except:
            pass


        self.extra_details=self.page.find("section",{"data-testid":"Details"}).find("div",{"data-testid":"title-details-section"})
        self.detail_parts=self.extra_details.find_all("li",class_="ipc-metadata-list__item")
        for self.each_part in self.detail_parts:
            try:
                self.part_label=self.each_part.find("span",class_="ipc-metadata-list-item__label").text
            except:
                if not "companycredits" in self.each_part["data-testid"]:
                    self.part_label=self.each_part.find("a",class_="ipc-metadata-list-item__label").text
            

            self.find_content=self.each_part.find("div",class_="ipc-metadata-list-item__content-container")
            try :
                if self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item") :
                    self.part_content=[self.each_one.text for self.each_one in  self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item")]

                else :
                    self.part_content=[self.each_one.text for self.each_one in self.find_content.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
            except:
                continue
            Filter_Base.movie_specs[self.movie_name][self.part_label]=self.part_content
        
       
        try:
            self.human_info=self.page.find("div",class_="Hero__ContentContainer-kvkd64-10").find("div",class_="Hero__MetaContainer__Video-kvkd64-4")
            self.find_information=self.human_info.find("div",class_="PrincipalCredits__PrincipalCreditsPanelWideScreen-hdn81t-0 iGxbgr")
            self.info_parts=self.find_information.find_all("li",class_="ipc-metadata-list__item")
            for self.each_one in self.info_parts:
                if self.each_one.find("span",class_="ipc-metadata-list-item__label")==None:
                    self.label_info=self.each_one.find("a",class_="ipc-metadata-list-item__label ipc-metadata-list-item__label--link").text
                else:
                    self.label_info=self.each_one.find("span",class_="ipc-metadata-list-item__label").text 

                self.content_info=[self.item.text for self.item in self.each_one.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
                Filter_Base.movie_specs[self.movie_name][self.label_info]=self.content_info
        except:pass
        return  Filter_Base.movie_specs


# obj=Filter_Base("https://www.imdb.com/search/title/?genres=action")
# obj.parse()
# print(obj.one_movie(obj.main_page,obj.movie_detail))