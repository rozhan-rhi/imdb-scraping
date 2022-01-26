from .filter_basic import Filter_Base
from ..filter_links import Link_Base


class User_Reviews(Filter_Base) :
    """checkout user review page
        in this class opinion_part is review"""
        
    def __init__(self,p_link):
        self.p_link=p_link
        
        
    def review(self):
        """we search in user reviews page and find reviews' contents"""
        #find all review items
        self.user_review_dict={}
        self.review_link=Link_Base(personal_link=self.p_link).opinion_review
        self.parse_award_link=super().parse_page(self.review_link)
        self.page_items=self.parse_award_link.find_all("div",class_="lister-item mode-detail imdb-user-review collapsable")
        self.num=0  #use this for counting reviews
        for self.each_item in self.page_items :
            self.num+=1
            self.main_table=self.each_item.find("div",class_="lister-item-content") #find the whole content of each review in main page
            self.opinion=self.main_table.a.text #find the title of review
            self.content=self.main_table.find("div",class_="content").div.text #find content of the opinion
            self.key_dict=f"idea {self.num}"    #create ideas keys for user_review_dict according num
            self.user_review_dict[self.key_dict]={}
            try :   #every reviews doesn't have rating
                self.rating_bar=self.main_table.find("div",class_="ipl-ratings-bar").span.text.replace("\n","").strip() #find rating of review
                self.user_review_dict[self.key_dict]["rating_bar"]=self.rating_bar  #save rating in dictionary
            except:pass
            self.user_review_dict[self.key_dict]["opinion"]=self.opinion     #save opinion in dictionary
            self.user_review_dict[self.key_dict]["content"]=self.content     #save content in dictionary
        return self.user_review_dict
