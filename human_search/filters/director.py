from ..information import Work_Info


class Director_Info(Work_Info):
    """save all information about director that includes work and biography"""

    def __init__(self,name):
        super().__init__(name)
        self.director_dict={}

    def __str__(self) :
        return f"all information about director is : \n {self.director_dict}"

    def director_work(self,activity):
        """shows the activity of director"""
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(activity)
        self.director_dict["activity"]=self.work_experience
        self.director_dict["known-for"]=self.known_for
        self.director_dict["expand "+activity]=self.movies

    def director_bio(self):
        """shows the biography of director"""
        self.director_overview=super().overview()
        self.director_family=super().family()
        self.director_dict["overview"]= self.director_overview
        self.director_dict["family"]=self.director_family