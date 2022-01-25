from .filter_basic import Filter_Base
from ..total_links import Link_Base


class User_Rating(Filter_Base) :
    """we search the rate of different group .
    in this class opinion_part is review"""
    def __init__(self,p_link) :
        self.p_link=p_link

        
    def rating_movie(self) :
        """we search in user rating page and find rating from different groups"""
        self.user_rating_dict={}
        self.rating_link=Link_Base(personal_link=self.p_link).opinion_rating
        self.parse_award_link=super().parse_page(self.rating_link)
        self.page_part=self.parse_award_link.find("section",class_="article listo")

        
        def imdb_user(self) :
            """find imdb users' rating of movie """
            try:
                self.label=self.page_part.find("div",class_="sectionHeading")
                self.each_label_name=self.label.text.strip()    #finds IMDB user word
                self.content_user=self.page_part.find("table",{"cellpadding":"0"}).find_all("tr")
                self.subject_content=self.content_user[0].text.strip().split()  #finds rating/votes words
                del self.content_user[0]
                self.general_measurement=self.page_part.find("div",{"align":"center"}).text.strip().replace("\n","")    #finds number of ratings
                self.general_measurement=" ".join(self.general_measurement.split()) 
                self.user_rating_dict["general_measurement"]=self.general_measurement
                
                self.range_number=[self.number for self.number in range(1,(len(self.content_user)+1))]
                for self.items_content , self.number in zip(self.content_user,self.range_number) :
                    self.items_types=self.items_content.find_all("td")
                    self.main_key=f"poll {self.number}"
                    self.user_rating_dict[self.main_key]={}
                    self.user_rating_dict[self.main_key][self.subject_content[0]]=self.items_types[0].text.strip()
                    self.user_rating_dict[self.main_key]["percent"]=self.items_types[1].text.strip()
                    self.user_rating_dict[self.main_key][self.subject_content[1]]=self.items_types[2].text.strip()
            except:pass
        imdb_user(self)

        
        def rating_demographic(self) :
            """finds rating of movie by demographic """
            try:
                self.tables=self.page_part.find_all("table")
                del self.tables[0]      #delete table of imdb user 
                for self.one_table in self.tables :
                    self.items_demographic=self.one_table.find_all("tr")    #finds different parts of rating tables 
                    self.type_category=self.items_demographic[0].text.strip().split("\n")   #age category / different types of users
                    del self.items_demographic[0]
                    for self.each_item_demographic in self.items_demographic :
                        self.parts_item=self.each_item_demographic.find_all("td")
                        self.seperator=self.tables.index(self.one_table)
                        if self.seperator==0 :
                            self.gender=self.parts_item[0].text.strip()    #find gender
                            del self.parts_item[0]
                            self.user_rating_dict[self.gender]={}  
                            self.numbers=[" = ".join(self.item.text.strip().replace("\n","").split()) for self.item in self.parts_item ] #finds the votes and rate in equal
                            for self.key,self.value in zip( self.type_category,self.numbers):
                                self.user_rating_dict[self.gender.strip()][self.key]=self.value.strip() 



                        if self.seperator!=0:
                            self.parts_item=[" = ".join(self.each_one.text.strip().replace("\n","").split()) for self.each_one in self.parts_item]
                            for self.key,self.value in zip(self.type_category,self.parts_item):
                                self.user_rating_dict[self.key]=self.value.strip() 
                                    
                                    
            except:pass
        rating_demographic(self)
        return self.user_rating_dict