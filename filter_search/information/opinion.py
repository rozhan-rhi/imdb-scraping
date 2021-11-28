from .filter_basic import Filter_Base
from ..total_links import Link_Base

class Movie_Opinion(Filter_Base) :
    """finds if the movie is winner in race , finds people' ideas about the movie and rating of movie"""
    
    def parse_award_page(self,main_url) :
        """parse the url of opinion part"""
        self.main_url=main_url
        self.base_page=super().main_page(super().parse_page(self.main_url))
        self.personal_link=super().get_personal_Link
        return self.personal_link
    
  

class User_Reviews(Movie_Opinion) :
    """checkout user review page
        in this class opinion_part is review"""
    
    def __init__(self,main_url):
        self.user_review_dict={}
        self.main_url=main_url
        
    def parse_completed_url(self) :
        self.page=super().parse_award_page(self.main_url)
        self.review_link=Link_Base(personal_link=self.page).opinion_review
        self.parse_award_link=super().parse_page(self.review_link)
        return self.parse_award_link


    def __str__(self) :
        return f"User Review of the movie is \n{self.user_review_dict}"
    
    def __call__(self) :
        self.title()
        self.review()
        return self.user_review_dict

    
    def title(self) :
        """we find user review word as a key of opinion_dict"""
        self.title_page=self.parse_completed_url().find("section",class_="article").h1.text #find user review word
        return self.title_page
    
    
    def review(self):
        """we search in user reviews page and find reviews' contents"""
        #find all review items
        self.page_items=self.parse_completed_url().find("div",class_="lister").find_all("div",class_="lister-item mode-detail imdb-user-review collapsable")
        self.num=0  #use this for counting reviews
        for self.each_item in self.page_items :
            self.num+=1
            self.main_table=self.each_item.find("div",class_="lister-item-content") #find the whole content of each review in main page
            self.opinion=self.main_table.a.text #find the title of review
            self.content=self.main_table.find("div",class_="content").find("div",class_="text show-more__control").text #find content of the opinion
            self.key_dict=f"idea {self.num}"    #create ideas keys for user_review_dict according num
            self.user_review_dict[self.key_dict]={}
            try :   #every reviews doesn't have rating
                self.rating_bar=self.main_table.find("div",class_="ipl-ratings-bar").span.text.replace("\n","").strip() #find rating of review
                self.user_review_dict[self.key_dict]["rating_bar"]=self.rating_bar  #save rating in dictionary
            except:pass
            self.user_review_dict[self.key_dict]["opinion"]=self.opinion     #save opinion in dictionary
            self.user_review_dict[self.key_dict]["content"]=self.content     #save content in dictionary
            
    


        
        

class User_Rating(Movie_Opinion) :
    """we search the rate of different group .
    in this class opinion_part is review"""
    
    def __init__(self,main_url) :
        self.user_rating_dict={}
        self.main_url=main_url
        
        
    def parse_completed_url(self) :
        self.page=super().parse_award_page(self.main_url)
        self.rating_link=Link_Base(personal_link=self.page).opinion_rating
        self.parse_award_link=super().parse_page(self.rating_link)
        return self.parse_award_link

    def __str__(self):
        return f"User Rating of movie is :\n{self.user_rating_dict}"
        
    def __call__(self) :
        self.title()
        self.rating_movie()
                    
        
    def title(self) :
        """we find user rating word as a key of opinion_dict"""
        self.page_part=self.parse_completed_url().find("section",class_="article")
        self.title_user=self.page_part.find("div",class_="subpage_title_block__right-column").h1.text   #find user rating word
        return self.title_user
    
    
    
        
    def rating_movie(self) :
        """we search in user rating page and find rating from different groups"""

        def imdb_user(self) :
            """find imdb users' rating of movie """
            self.label=self.page_part.find("div",class_="sectionHeading")
            self.each_label_name=self.label.text.strip()    #finds IMDB user word
            self.main_part=self.page_part.find("div",class_="title-ratings-sub-page")
            self.content_user=self.main_part.find("div",class_="allText").find("table",{"cellpadding":"0"}).find_all("tr")
            self.subject_content=self.content_user[0].text.strip().split()  #finds rating/votes words
            del self.content_user[0]
            self.general_measurement=self.main_part.find("div",{"align":"center"}).text.strip().replace("\n","")    #finds number of ratings
            self.general_measurement=" ".join(self.general_measurement.split()) 
            self.user_rating_dict["general_measurement"]=self.general_measurement
            
            for self.items_content in self.content_user :
                self.items_types=self.items_content.find_all("td")

                for self.number in range(1,(len(self.items_content)+1)) :
                    self.main_key=f"poll {self.number}"
                    self.user_rating_dict[self.main_key]={}
                    self.user_rating_dict[self.main_key][self.subject_content[0]]=self.items_types[0].text.strip()
                    self.user_rating_dict[self.main_key]["percent"]=self.items_types[1].text.strip()
                    self.user_rating_dict[self.main_key][self.subject_content[1]]=self.items_types[2].text.strip()
        imdb_user(self)
        
        
        def rating_demographic(self) :
            """finds rating of movie by demographic """
                
            self.tables=self.main_part.find_all("table")
            del self.tables[0]      #delete table of imdb user 
            for self.table_one in self.tables :
                self.items_demographic=self.table_one.find_all("tr")    #finds different parts of rating tables 
                self.type_category=self.items_demographic[0].text.strip().split("\n")   #age category / different types of users
                del self.items_demographic[0]
                for self.each_item_demographic in self.items_demographic :
                    self.parts_each_item=self.each_item_demographic.find_all("td")
                    self.seperator=self.tables.index(self.table_one)
                    if self.seperator==0 :
                        self.gender=self.parts_each_item[0].text.strip()    #find gender
                        del self.parts_each_item[0]
                        self.user_rating_dict[self.gender]={}  


                            
                    for self.each_part in self.parts_each_item :
                        self.content_demographic=self.each_part.text.strip().replace("\n","")   #finds the votes 
                        self.content_demographic=" = ".join(self.content_demographic.split())
                        for self.each_type in self.type_category :
                            self.each_type=self.each_type.strip()
                            if self.each_type.lower()=="all ages" :
                                self.user_rating_dict[self.gender.strip()][self.each_type]=self.content_demographic.strip() 
                                  
                            elif self.seperator!=0:
                                self.user_rating_dict[self.each_type]=self.content_demographic.strip() 
                                
                                
                            else : 
                                self.each_type=f"age {self.each_type.strip()}"
                                self.user_rating_dict[self.gender.strip()][self.each_type]=self.content_demographic.strip()
                                
        rating_demographic(self)
    
    
                


                
            
        
