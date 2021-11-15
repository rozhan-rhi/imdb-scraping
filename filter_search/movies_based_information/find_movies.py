from . import Save_Info
class Movies(Save_Info):

    def several_movie(self,url):
        """gets 2 functions as parameter and finds all contents of some movies"""
        self.total={}
        self.url=url
        self.list_movies=super().parse_page(self.url).find_all("div",class_="lister-item mode-advanced") #finds all movies in a page
        for self.each_movie in self.list_movies :
            self.total_text=self.each_movie.find("div",class_="lister-item-content") #finds each movie part
            self.specification=super().movie_detail(super().main_page(self.total_text)) #uses 2 functions in parameter to finds all contents of movies
            self.each_movie_name=super().movie_name(self.total_text)
            self.total[self.each_movie_name]=self.specification
        return self.total  



    def one_movie(self,url):
        """gets 2 functions as parameter and finds all contents of one movie"""
        self.total={}
        self.url=url
        self.movie=super().parse_page(self.url).find("div",class_="lister-item mode-advanced")    #finds first movie
        self.total_text=self.movie.find("div",class_="lister-item-content")  #finds the movie part
        self.specification=super().movie_detail(super().main_page(self.total_text))  #uses 2 functions in parameter to finds all contents of movie
        self.each_movie_name=super().movie_name(self.total_text)
        self.total[self.each_movie_name]=self.specification
        return self.total  

