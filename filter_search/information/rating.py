
class Movie_Rating() :
    """finds the rate of movie"""
    
    def __init__(self,page) :
        self.page=page 
                
                    
    def rating(self) :  
        try:
            #finds the rate of movie
            self.rating_part=self.page.find("div",class_="RatingBar__ButtonContainer-sc-85l9wd-1 idYUsR").find("div",class_="AggregateRatingButton__ContentWrap-sc-1ll29m0-0").span.text 
            return self.rating_part 
        except:
            pass

    def __call__(self) :
        self.rating()
            self.rating_part=self.page.find("div",class_="RatingBar__ButtonContainer-sc-85l9wd-1 idYUsR").find("div",class_="AggregateRatingButton__ContentWrap-sc-1ll29m0-0").span.text  
            return self.rating_part
        except:
            pass

