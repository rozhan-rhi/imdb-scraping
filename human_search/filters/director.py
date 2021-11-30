from ..information import Work_Info


class Director_Info(Work_Info):
    """save all information about director that includes work and biography"""

    def __init__(self,name,activity):
        super().__init__(name)
        self.director_dict={}
        self.activity=activity


    def __call__(self) :
        self.director_bio()
        self.director_work()
        return self.director_dict

    def director_work(self):
        """shows the activity of director"""
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(self.activity)
        self.director_dict["activity"]=self.work_experience
        self.director_dict["known-for"]=self.known_for
        self.director_dict["expand "+self.activity]=self.movies

    def director_bio(self):
        """shows the biography of director"""
        self.director_overview=super().overview()
        self.director_family=super().family()
        self.director_salary=super().salary()
        self.director_dict["overview"]= self.director_overview
        self.director_dict["family"]=self.director_family
        self.director_dict["salary"]=self.director_salary