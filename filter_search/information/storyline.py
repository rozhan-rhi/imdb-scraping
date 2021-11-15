class Movie_Storyline :
    """finds summary and genre,... of movie"""
    
    def __init__(self,page) :
        self.storyline_dict={}
        self.page=page
        
    def calling(self):
        self.genre()
        return self.storyline_dict
        
        
    def genre(self):
        self.find_genre=self.page.find("li",{"data-testid":"storyline-genres"}) #finds genre part
        self.genre_label=self.find_genre.span.text  #finds title(genre)
        self.genre_content=[self.item.a.text for self.item in self.find_genre.find_all("li",role="presentation")]   #finds all genre types of movie
        self.storyline_dict[self.genre_label]=self.genre_content    
