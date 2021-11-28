from ..information import *
from ..total_links import Link_Base


class Save_Info(Filter_Base):
    """save all information about movie """
    def __init__(self,main_url) :
        self.movie_specs={}  #save all movies with their details  
        self.main_url=main_url   
    
    def movie_name(self):
        self._page_main_url=super().main_page(super().parse_page(self.main_url))
        self.name=self._page_main_url.h1.text #finds the name of movie
        return self.name
    
    @property
    def get_page(self) :
        return self._page_main_url
    
    def calling_classes(self):  
        self.movie_name()      
        self.obj_details=Movie_Details(self.get_page)
        self.obj_participant=Movie_Participant(self.get_page)
        self.obj_rating=Movie_Rating(self.get_page)
        self.obj_runtime=Movie_Runtime(self.get_page)
        self.obj_storyline=Movie_Storyline(self.get_page)
        
        self.movie_specs["Movie_Details"]=self.obj_details()
        self.movie_specs["Movie_Participant"]=self.obj_participant()
        self.movie_specs["Movie_Rating"]=self.obj_rating()
        self.movie_specs["Movie_Runtime"]=self.obj_runtime()
        self.movie_specs["Movie_Storyline"]=self.obj_storyline()
        
        
    def __call__(self) :
        return self.movie_specs
        
# obj=Save_Info()
# obj2=Filter_Base()
# print(obj.calling_classes(obj2.main_page(obj2.parse_page("https://www.imdb.com/search/title/?genres=crime"))))