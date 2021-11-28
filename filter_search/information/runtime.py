
class Movie_Runtime():
    """find the time of the movie"""
    
    def __init__(self,page):
        self.page=page
        self.runtime_dict={}

            
    def runtime(self) :
        try:
            #finds runtime part
            self.runtime_part=self.page.find("section",{"data-testid":"TechSpecs"}).find("li",{"data-testid":"title-techspec_runtime"})   
            self.runtime_label=self.runtime_part.find("span",class_="ipc-metadata-list-item__label").text   #finds the title
            #finds the time of movie
            self.runtime_content=self.runtime_part.find("div",class_="ipc-metadata-list-item__content-container")
            if self.runtime_content.find("span",class_="ipc-metadata-list-item__list-content-item"):
                self.time_movie=self.runtime_content.find("span",class_="ipc-metadata-list-item__list-content-item").text 
            else:
                self.time_movie=self.runtime_content.text
            self.runtime_dict[self.runtime_label]=self.time_movie
        except:pass
    
    def __call__(self) :
        self.runtime()
        return self.runtime_dict