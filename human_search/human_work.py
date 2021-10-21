from human_info_basic import Human_Basic
from links_human import Links

class Work_Info(Human_Basic) :
    """finds information about person's work activity"""

    work_dict={}

    def __init__(self,name):
        super().__init__(name)
        Work_Info.work_dict[self.name]={}
         

    def __str__(self):
        return f"the work experience of {self.name} is : \n{Work_Info.work_dict}"


    def common(self) :
        """common part between methods that returns a page that is used in other methods"""
        self.person_link=self.personal_link()
        self.url=Links(special_link=self.person_link).work_url #get work url from links_human.py
        self.page=super().common_parsing(self.url)
        self.tables=self.page.find_all("div",class_="article")  #finds diffrent tables in a page



    def filmography(self):
        """finds all work experiences of person"""
        self.common()
        self.credit_list=[]
        for self.each_table in self.tables :
            try:
                if self.each_table.h2.text=="Filmography":  #finds filmography table
                    for self.each_part in self.each_table.find_all("div",class_="head"):    #finds different parts of activity
                        self.extra_text="".join([self.one.text for self.one in self.each_part.find_all("span")])    #finds extra texts in span tags
                        self.credit=self.each_part.text.replace("\n","").replace(self.extra_text,"")    #delete extra texts and "\n" of the whole of text
                        self.credit_list.append(self.credit)
            except:pass
        Work_Info.work_dict[self.name]["activity"]=self.credit_list
        return self.credit_list


    def movies_work(self,job):
        """since a person can have several jobs,you can find the movies and their release dates
         according to any job(producer,actor,director,writer,...) of that person"""
        self.movies_list=[]
        self.common()
        for self.each_table in self.tables :
            try:
                if self.each_table.h2.text=="Filmography":  #finds filmography table
                    self.all_movies=self.each_table.find_all("div",class_="filmo-row") #finds all movies in all parts
                    for self.one_movie in self.all_movies:
                        if job in self.one_movie["id"]:    #finds movies that their id include job
                            #finds the name of movie and its release date
                            self.movie_name=(self.one_movie.a.text+self.one_movie.span.text).replace("\n"," ").encode("ascii","ignore").decode("utf-8")
                            self.movies_list.append(self.movie_name)
            except:pass
        Work_Info.work_dict[self.name]["expand "+job]=self.movies_list
        return self.movies_list



    def known(self):
        """finds movies that makes person known for"""
        self.known_list=[]
        self.common()
        for self.each_table in self.tables :
            try:
                if self.each_table.h2.text=="Known For":    #finds known for table
                    self.movies_table=self.each_table.find_all("div",class_="knownfor-title")   #finds all parts of known for table
                    for self.each_table in self.movies_table :
                        self.movie_name=self.each_table.find("div",class_="knownfor-title-role").a.text.strip()     #finds the name of movie
                        self.known_list.append(self.movie_name)
            except:pass
        Work_Info.work_dict[self.name]["known-for"]=self.known_list
        return self.known_list



