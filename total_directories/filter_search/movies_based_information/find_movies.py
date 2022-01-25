from .saving_info import Save_Info
import re

class Movies(Save_Info):

    def several_movie(self,url):
        """gets 2 functions as parameter and finds all contents of some movies"""
        self.total={}
        self.url=url
        self.movie_url=[self.each.a for self.each in super().parse_page(self.url).find_all("div",class_="lister-item-content")]
        for self.each_movie in self.movie_url :
            self.complete_url=f"https://www.imdb.com{self.each_movie['href']}"
            self.specification=super().calling_classes(self.complete_url,self.each_movie['href']) #uses 2 functions in parameter to finds all contents of movies
            self.each_movie_name=self.each_movie.text
            self.total[self.each_movie_name]=self.specification
        return self.total



    def one_movie(self,url):
        """gets 2 functions as parameter and finds all contents of one movie"""
        self.total={}
        self.url=url
        self.movie=super().parse_page(self.url)    #finds first movie
        self.total_text=self.movie.find("div",class_="lister-item-content")  #finds the movie part
        self.href_link=self.total_text.a["href"]
        self.complete_url=f"https://www.imdb.com{self.href_link}"
        self.specification=super().calling_classes(self.complete_url,self.href_link)  #uses 2 functions in parameter to finds all contents of movie
        self.each_movie_name=super().movie_name(self.total_text)
        self.total[self.each_movie_name]=self.specification
        return self.total  

