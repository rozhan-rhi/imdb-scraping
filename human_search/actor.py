from human_work import Work_Info

class Actor_Info(Work_Info):

    actor_dict={}

    def __init__(self,name):
        super().__init__(name)

    def __str__(self) :
        return f"all information about actor is : \n {Actor_Info.actor_dict}"

    def actor_work(self,activity):
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(activity)
        Actor_Info.actor_dict["activity"]=self.work_experience
        Actor_Info.actor_dict["known-for"]=self.known_for
        Actor_Info.actor_dict["expand "+activity]=self.movies

    def actor_bio(self):
        self.actor_overview=super().overview()
        self.actor_family=super().family()
        Actor_Info.actor_dict["overview"]= self.actor_overview
        Actor_Info.actor_dict["family"]=self.actor_family
    
