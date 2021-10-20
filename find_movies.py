from filter_basic import Filter_Base

class Movies(Filter_Base):
    def several_movie(self,url):
        """gets 2 functions as parameter and finds all contents of some movies"""
        self.list_movies=super().parse_page(url).find_all("div",class_="lister-item mode-advanced") #finds all movies in a page
        for self.each_movie in self.list_movies :
            self.movie_content=self.each_movie.find("div",class_="lister-item-content") #finds each movie part
            self.total_content=super().movie_detail(super().main_page(self.movie_content)) #uses 2 functions in parameter to finds all contents of movies
        return  self.total_content



    def one_movie(self,url):
        """gets 2 functions as parameter and finds all contents of one movie"""
        self.movie=super().parse_page(url).find("div",class_="lister-item mode-advanced")    #finds first movie
        self.movie_content=self.movie.find("div",class_="lister-item-content")  #finds the movie part
        self.total_content=super().movie_detail(super().main_page(self.movie_content))  #uses 2 functions in parameter to finds all contents of movie
        return  self.total_content

