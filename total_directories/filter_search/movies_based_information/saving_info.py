from ..information.filter_basic import Filter_Base
from ..information.details import Movie_Details
from ..information.participant import Movie_Participant
from ..information.rating import Movie_Rating
from ..information.runtime import Movie_Runtime
from ..information.story_line import Movie_Storyline
from ..information.opinion import *

class Save_Info(Filter_Base):
    """save all information about movie """

    
    # def movie_name(self,parse_text):
    #     self.finding_name=parse_text
    #     self.name=self.finding_name.h3.a.text #finds the name of movie
    #     return self.name
    
    def calling_classes(self,url,personal):
        self.movie_specs={}  #save all movies with their details  
        self.personal=personal
        self.page=super().parse_page(url)
        # self.special_part=super().get_personal_Link
        # self.obj_details=Movie_Details(self.page)
        # self.obj_participant=Movie_Participant(self.page)
        # self.obj_rating=Movie_Rating(self.page)
        # self.obj_runtime=Movie_Runtime(self.page)
        # self.obj_storyline=Movie_Storyline(parse_url=self.page,p_link=self.personal)
        # self.obj_opinion_award=Awards(self.personal)
        # self.obj_opinion_review=User_Reviews(self.personal)
        self.obj_opinion_rating=User_Rating(self.personal)
        
        
        # self.movie_specs["runtime"]=self.obj_runtime.runtime()
        # self.movie_specs["genre"]=self.obj_storyline.genre()
        # self.movie_specs["rating"]=self.obj_rating.rating()
        # self.movie_specs["summary"]=self.obj_storyline.summary()
        # self.movie_specs["movie_tag"]=self.obj_storyline.movie_tag()
        # self.movie_specs["participant"]=self.obj_participant.people()
        # self.movie_specs["detail"]=self.obj_details.detail_part()
        # self.movie_specs["parent_guide"]=self.obj_storyline.movie_parents_guide()
        # self.movie_specs["awards"]=self.obj_opinion_award.awards_page()
        # self.movie_specs["user-reviews"]=self.obj_opinion_review.review()
        self.movie_specs["user-rating"]=self.obj_opinion_rating.rating_movie()
        print(self.movie_specs["user-rating"])
        return self.movie_specs
        
