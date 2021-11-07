from human_work import Work_Info

class Writer_Info(Work_Info):
    """save all information about writer that includes work and biography"""

    def __init__(self,name):
        super().__init__(name)
        self.writer_dict={}

    def __str__(self) :
        return f"all information about writer is : \n {self.writer_dict}"

    def writer_work(self,activity):
        """shows the activity of writer"""
        self.work_experience=super().filmography()
        self.known_for=super().known()
        self.movies=super().movies_work(activity)
        self.writer_dict["activity"]=self.work_experience
        self.writer_dict["known-for"]=self.known_for
        self.writer_dict["expand "+activity]=self.movies

    def writer_bio(self):
        """shows the biography of writer"""
        self.writer_overview=super().overview()
        self.writer_family=super().family()
        self.writer_dict["overview"]= self.writer_overview
        self.writer_dict["family"]=self.writer_family
    

