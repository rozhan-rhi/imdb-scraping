from ..information import *
from ..total_links import Link_Base


class Save_Info(Filter_Base):
    """save all information about movie """
    
    def movie_name(self,main_page):
        self.main_page=main_page
        self.name=self.main_page.h3.a.text #finds the name of movie
        return self.name
    

    
    def calling_classes(self,base_page): 
        self.movie_specs={}  #save all movies with their details  
 
        self.base_page=super().main_page(base_page)
        self.personal_link=super().get_personal_Link
        
        self.obj_details=Movie_Details(self.base_page)
        self.obj_participant=Movie_Participant(self.base_page)
        self.obj_rating=Movie_Rating(self.base_page)
        self.obj_runtime=Movie_Runtime(self.base_page)
        self.obj_storyline=Movie_Storyline(self.base_page)
        self.obj_opinion_rating=User_Rating(p_link=self.personal_link)
        # self.obj_opinion_review=User_Reviews(p_link=self.personal_link)
        
        self.movie_specs["Movie Details"]=self.obj_details()
        self.movie_specs["Movie Participant"]=self.obj_participant()
        self.movie_specs["Movie Rating"]=self.obj_rating.rating()
        self.movie_specs["Movie Runtime"]=self.obj_runtime.runtime()
        self.movie_specs["Movie Storyline"]=self.obj_storyline()
        self.movie_specs["User Rating"]=self.obj_opinion_rating()
        # self.movie_specs["User Review"]=self.obj_opinion_review()
        return self.movie_specs

        
        
