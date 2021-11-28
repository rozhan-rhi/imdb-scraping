import requests
from bs4 import BeautifulSoup
from .find_movies import Movies
from .callbacks import Custom_Callback
from ..total_links import Link_Base
 

class Filters(Link_Base,Movies) :
    """the class includes callback functions .all callbacks use in several_movie function except movie_name_filter_callback
    movie_name_filter_callback uses in one_movie function"""
    
    # def __str__(self) :
    #     return "this class finds movies and their details based on filters"

    
    def rating_filter(self,start,end,adult=None) :
        """find movies based on rating . it gets three parameters, first two parameters are range of rating and last one is adult limit """
        self.url=Link_Base(rating_start=start,rating_end=end,adult_limit=adult).rating_url  #get the rating url from links.py
        self.content_url=super().several_movie(self.url)
        # callback_func(self.content_url)
        return self.content_url


    def movie_name_filter(self,name,callback_func=None):
        """find all information about the movie by its name"""
        self.url=Link_Base(movie_name=name).movie_name_url #get the movie_name url from links.py
        self.content_url=super().one_movie(self.url)
        # callback_func(self.content_url)
        return self.content_url


    def genre_filter(self,genre_name,adult=None,callback_func=None):
        """find movies based on their generes"""
        self.url=Link_Base(genre_name=genre_name,adult_limit=adult).genre_url   #get the genre url from links.py
        self.content_url=super().several_movie(self.url)
        # callback_func(self.content_url)
        return self.content_url

    def release_date_filter(self,start,end,adult=None,callback_func=None):
        """find movies based on their release dates.2 first parameters are the range of dates"""
        self.url=Link_Base(date_start=start,date_end=end,adult_limit=adult).release_url    #get the release date url from links.py
        self.content_url=super().several_movie(self.url)
        # callback_func(self.content_url)
        return self.content_url

    def country_filter(self,country_name,adult=None,callback_func=None) :
        """find movies based on the country movies produced"""
        self.base_url=Link_Base(country_name=country_name).advanced_url      #get the country url from links.p
        self.response_=requests.get(self.base_url)
        self.parse=BeautifulSoup(self.response_.text,"html.parser")
        self.page_labels=self.parse.find_all("div",class_="clause") #find all parts of advanced search page
        for self.label in self.page_labels:
            if self.label.h3.text=="Countries":     #find countries label
                self.country_options=self.label.find_all("option")     #find all countries option
                for self.each_option in self.country_options:
                    if self.each_option.text.lower()==country_name.lower() :    #find the country that match with country_name in parameter
                        self.country_brief=self.each_option["value"]    #find the abbreviation of the name of country
                
        try :
            self.url=Link_Base(country_name=self.country_brief,adult_limit=adult).country_url
            self.content_url=super().several_movie(self.url)
            callback_func(self.content_url)
            return self.content_url
        except: #if country_name parameter wasn't find , it will returns all countries' names
            self.total_countries=[self.each_country.text for self.each_country in self.country_options]
            return self.total_countries 