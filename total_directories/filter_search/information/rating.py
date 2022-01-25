class Movie_Rating :
    """finds the rate of movie"""
    
    def __init__(self,page) :
        self.page=page 
                
                    
    def rating(self) :  
        try:
            #finds the rate of movie
            self.rating_part=list(set([self.each_tag.span.text for self.each_tag in self.page.find_all("a",href=True) if "/ratings/" in self.each_tag["href"]])).pop()
            return self.rating_part
        except:
            pass