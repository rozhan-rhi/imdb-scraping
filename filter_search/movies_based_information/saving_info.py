from information import Filter_Base
from information import Movie_Storyline

class Save_Info(Filter_Base):
    """save all information about movie """
    
    def movie_name(self,parse_text):
        self.finding_name=parse_text
        self.name=self.finding_name.h3.a.text #finds the name of movie
        return self.name
    
    def calling_classes(self,page):
        self.movie_specs={}  #save all movies with their details        
        # self.obj_details=Movie_Details(page)
        # self.obj_participant=Movie_Participant(page)
        # self.obj_rating=Movie_Rating(page)
        # self.obj_runtime=Movie_Runtime(page)
        self.obj_storyline=Movie_Storyline(page)
        return self.obj_storyline.calling()
        
obj=Save_Info()
obj2=Filter_Base()
print(obj.calling_classes(obj2.main_page(obj2.parse_page("https://www.imdb.com/search/title/?genres=crime"))))