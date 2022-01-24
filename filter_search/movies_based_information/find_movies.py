from .saving_info import Save_Info
import re

class Movies(Save_Info):

    def several_movie(self,url):
        """gets 2 functions as parameter and finds all contents of some movies"""
        self.total={}
        self.url=url
        self.movie_url=[self.each for self.each in super().parse_page(self.url).find_all("a",href=True) if re.findall("tt([0-9]+)" , self.each['href'])]
        for self.each_movie in self.movie_url :
            self.complete_url=f"https://www.imdb.com{self.each_movie['href']}"
            print(self.complete_url)
        #     self.specification=super().calling_classes(self.complete_url,self.each_movie['href']) #uses 2 functions in parameter to finds all contents of movies
        #     self.each_movie_name=self.each_movie.text
        #     self.total[self.each_movie_name]=self.specification
        # return self.total



    def one_movie(self,url):
        """gets 2 functions as parameter and finds all contents of one movie"""
        self.total={}
        self.url=url
        self.movie=super().parse_page(self.url).find("div",class_="lister-item mode-advanced")    #finds first movie
        self.total_text=self.movie.find("div",class_="lister-item-content")  #finds the movie part
        self.specification=super().calling_classes(self.total_text)  #uses 2 functions in parameter to finds all contents of movie
        self.each_movie_name=super().movie_name(self.total_text)
        self.total[self.each_movie_name]=self.specification
        return self.total  

