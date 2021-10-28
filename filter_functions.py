from links import Link_Base
from find_movies import Movies
import requests
from bs4 import BeautifulSoup


class Filters_Sub(Movies,Link_Base) :
    
    def __str__(self) :
        return "this class finds movies and their details based on filters"

    def common_part(self,url) :
        """parse the url of function in parameter and use several_movie method to return the dict of movies and their details
        it's common among filters except movie_name_filter"""
        self.total_info=super().several_movie(url) #use several_movie method to find movies' names and  their contents 
        return self.total_info


    
    def rating_filter(self,start,end,adult=None) :
        """find movies based on rating . it gets three parameters, first two parameters are range of rating and last one is adult limit """
        self.url=Link_Base(rating_start=start,rating_end=end,adult_limit=adult).rating_url  #get the rating url from links.py
        return self.common_part(self.url)


    def movie_name_filter(self,name):
        """find all information about the movie by its name"""
        self.url=Link_Base(movie_name=name).movie_name_url #get the movie_name url from links.py
        self.total_info=super().one_movie(self.url)   #use one_movie method to find movie's name and its content
        return self.total_info


    def genre_filter(self,genre_name,adult=None):
        """find movies based on their generes"""
        self.url=Link_Base(genre_name=genre_name,adult_limit=adult).genre_url   #get the genre url from links.py
        return self.common_part(self.url)


    def release_date_filter(self,start,end,adult=None):
        """find movies based on their release dates.2 first parameters are the range of dates"""
        self.url=Link_Base(date_start=start,date_end=end,adult_limit=adult).release_url    #get the release date url from links.py
        return self.common_part(self.url)


    def country_filter(self,country_name,adult=None) :
        """find movies based on the country movies produced"""
        self.base_url=Link_Base().advanced_url      #get the country url from links.p
        self.req=requests.get(self.base_url)
        self.parse=BeautifulSoup(self.req.text,"html.parser")
        self.page_labels=self.parse.find_all("div",class_="clause") #find all parts of advanced search page
        for self.label in self.page_labels:
            if self.label.h3.text=="Countries":     #find countries label
                self.country_options=self.label.find_all("option")     #find all countries option
                for self.each_option in self.country_options:
                    if self.each_option.text.lower()==country_name :    #find the country that match with country_name in parameter
                        self.country_brief=self.each_option["value"]    #find the abbreviation of the name of country
        self.url=Link_Base(country_name=self.country_brief,adult_limit=adult).country_url
        return self.common_part(self.url)