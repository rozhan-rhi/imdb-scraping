from ..information.human_work import Work_Info

class Actor_Info(Work_Info):
    """save all information about actor that includes work and biography"""


    def __init__(self,name,activity):
        super().__init__(name)
        self.actor_dict={}
        self.activity=activity

    def __call__(self) :
        self.actor_bio()
        self.actor_work()
        return self.actor_dict
    
    
    def actor_work(self):
        """shows the activity of actor"""
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(self.activity)
        self.actor_dict["activity"]=self.work_experience
        self.actor_dict["known-for"]=self.known_for
        self.actor_dict["expand "+self.activity]=self.movies

    def actor_bio(self):
        """shows the biography of actor"""
        self.actor_overview=super().overview()
        self.actor_family=super().family()
        self.actor_salary=super().salary()
        self.actor_dict["overview"]= self.actor_overview
        self.actor_dict["family"]=self.actor_family
        self.actor_dict["salary"]=self.actor_salary
