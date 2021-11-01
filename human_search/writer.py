from human_work import Work_Info

class Writer_Info(Work_Info):

    writer_dict={}

    def __init__(self,name):
        super().__init__(name)

    def __str__(self) :
        return f"all information about writer is : \n {Writer_Info.writer_dict}"

    def writer_work(self,activity):
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(activity)
        Writer_Info.writer_dict["activity"]=self.work_experience
        Writer_Info.writer_dict["known-for"]=self.known_for
        Writer_Info.writer_dict["expand "+activity]=self.movies

    def writer_bio(self):
        self.writer_overview=super().overview()
        self.writer_family=super().family()
        Writer_Info.writer_dict["overview"]= self.writer_overview
        Writer_Info.writer_dict["family"]=self.writer_family
    

