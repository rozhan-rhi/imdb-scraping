from .filter_basic import Filter_Base
import re
class Movie_Participant(Filter_Base):
    """finds the name of the humans of movie"""
    
    def __init__(self,page) :
        self.page=page
        
        
    def people(self):
        self.people_dict={}
        self.info_parts=self.page.find_all("li",{"data-testid":"title-pc-principal-credit"}) #finds different parts of human table
        for self.each_one in self.info_parts:
            try: 
                self.info=self.each_one.span
                self.label_info=self.info.text
                self.content=[self.each_name.text for self.each_name in self.each_one.find_all("a",href=True) if "name" in self.each_name['href'].split("/")]
                self.people_dict[self.label_info]=self.content
                
            except:
                self.info=self.each_one.find("a",href=True)
                self.label_info=self.info.text 
                self.see_full_page=self.parse_page(f"https://www.imdb.com{self.info['href']}").find("table",class_="cast_list")
                self.all_options=list(filter(None,[self.name_movie.text.strip().replace("\n","") for self.name_movie in self.see_full_page.find_all("a",href=True) if "name" in self.name_movie['href'].split("/")]))
                self.content=self.all_options
                self.people_dict[self.label_info]=self.content
        return self.people_dict
