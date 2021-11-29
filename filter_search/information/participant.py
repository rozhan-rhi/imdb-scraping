from .filter_basic import Filter_Base
class Movie_Participant(Filter_Base):
    """finds the name of the humans of movie"""
    
    def __init__(self,page) :
        self.page=page
        
        
    def people(self):
        self.people_dict={}
        try: 
            self.human_info=self.page.find("div",class_="Hero__ContentContainer-kvkd64-10") #finds human table
            self.find_information=self.human_info.find("div",class_="PrincipalCredits__PrincipalCreditsPanelWideScreen-hdn81t-0 iGxbgr") #one step closer
            self.info_parts=self.find_information.find_all("li",class_="ipc-metadata-list__item") #finds different parts of human table
            for self.each_one in self.info_parts:
                if self.each_one.find("span",class_="ipc-metadata-list-item__label")==None: #this if/else for finding label of each part
                    self.label_info=self.each_one.find("a",class_="ipc-metadata-list-item__label ipc-metadata-list-item__label--link").text
                else:
                    self.label_info=self.each_one.find("span",class_="ipc-metadata-list-item__label").text 

                if self.label_info.lower()=="stars":
                    self.star_link=(self.each_one.find("a",class_="ipc-metadata-list-item__icon-link"))["href"]
                    self.all_actor_link=f"https://www.imdb.com{self.star_link}"
                    self.actor_page=super().parse_page(self.all_actor_link)
                    self.actors_table=self.actor_page.find("table",class_="cast_list").find_all("tr")
                    self.actors_names=[]
                    for self.each_table in self.actors_table:
                        try:
                            self.delete_option=self.each_table.find("td",class_="primary_photo")
                            self.all_options=self.each_table.find_all("td")
                            for self.each_option in self.all_options:
                                if "name" in self.each_option.a["href"] :
                                    if self.each_option!=self.delete_option:
                                        self.name=self.each_option.a.text
                                        self.actors_names.append(self.name.strip().replace("\n",""))
                        
                        except:pass
                    self.people_dict["actor"]=self.actors_names
                    

                else:
                    #finds the content of each part
                    self.content_info=[self.item.text for self.item in self.each_one.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
                    self.people_dict[self.label_info]=self.content_info
        except:pass
        
        return self.people_dict