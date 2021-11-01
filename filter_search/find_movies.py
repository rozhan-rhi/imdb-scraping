from typing import MutableSet
from filter_basic import Filter_Base
from filter_funcs_callback import Filters_Callback
class Movies(Filter_Base):

    total={}

    def several_movie(self,callback):
        """gets 2 functions as parameter and finds all contents of some movies"""
        self.url=callback
        self.list_movies=super().parse_page(self.url).find_all("div",class_="lister-item mode-advanced") #finds all movies in a page
        for self.each_movie in self.list_movies :
            self.total_text=self.each_movie.find("div",class_="lister-item-content") #finds each movie part
            self.specification=super().movie_detail(super().main_page(self.total_text)) #uses 2 functions in parameter to finds all contents of movies
            self.each_movie_name=super().movie_name(self.total_text)
            Movies.total[self.each_movie_name]=self.specification
        return Movies.total  



    def one_movie(self,callback):
        """gets 2 functions as parameter and finds all contents of one movie"""
        self.url=callback
        self.movie=super().parse_page(self.url).find("div",class_="lister-item mode-advanced")    #finds first movie
        self.total_text=self.movie.find("div",class_="lister-item-content")  #finds the movie part
        self.specification=super().movie_detail(super().main_page(self.total_text))  #uses 2 functions in parameter to finds all contents of movie
        self.each_movie_name=super().movie_name(self.total_text)
        Movies.total[self.each_movie_name]=self.specification
        return Movies.total  

obj=Movies()
obj2=Filters_Callback()
print(obj.one_movie(obj2.movie_name_filter_callback("squid game")))