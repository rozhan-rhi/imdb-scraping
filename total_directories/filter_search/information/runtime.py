class Movie_Runtime:
    """find the time of the movie"""
    
    def __init__(self,page):
        self.page=page

            
    def runtime(self) :
        try:
            #finds runtime part
            self.runtime_part=self.page.find("li",{"data-testid":"title-techspec_runtime"})   
            #finds the time of movie
            self.runtime_content=self.runtime_part.find("div",class_="ipc-metadata-list-item__content-container")
            if self.runtime_content.find("span",class_="ipc-metadata-list-item__list-content-item"):
                self.time_movie=self.runtime_content.find("span",class_="ipc-metadata-list-item__list-content-item").text 
            else:
                self.time_movie=self.runtime_content.text
            return self.time_movie
        except:pass