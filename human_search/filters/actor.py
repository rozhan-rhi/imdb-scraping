from ..information import Work_Info

class Actor_Info(Work_Info):
    """save all information about actor that includes work and biography"""


    def __init__(self,name):
        super().__init__(name)
        self.actor_dict={}

    def __str__(self) :
        return f"all information about actor is : \n {self.actor_dict}"

    def actor_work(self,activity):
        """shows the activity of actor"""
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(activity)
        self.actor_dict["activity"]=self.work_experience
        self.actor_dict["known-for"]=self.known_for
        self.actor_dict["expand "+activity]=self.movies

    def actor_bio(self):
        """shows the biography of actor"""
        self.actor_overview=super().overview()
        self.actor_family=super().family()
        self.actor_dict["overview"]= self.actor_overview
        self.actor_dict["family"]=self.actor_family
    
