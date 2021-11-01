from human_work import Work_Info


class Director_Info(Work_Info):

    director_dict={}

    def __init__(self,name):
        super().__init__(name)

    def __str__(self) :
        return f"all information about director is : \n {Director_Info.director_dict}"

    def director_work(self,activity):
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(activity)
        Director_Info.director_dict["activity"]=self.work_experience
        Director_Info.director_dict["known-for"]=self.known_for
        Director_Info.director_dict["expand "+activity]=self.movies

    def director_bio(self):
        self.director_overview=super().overview()
        self.director_family=super().family()
        Director_Info.director_dict["overview"]= self.director_overview
        Director_Info.director_dict["family"]=self.director_family
    
class Rozhan():
    s=Work_Info()
    