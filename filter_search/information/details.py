# from imdbscraping.filter_search.information.filter_basic import Filter_Base
class Movie_Details :
    """finds details of movie like release date,country of origin,language,..."""
    
    def __init__(self,page) :
        self.page=page
        self.detail_dict={}

    
    def detail_part(self):
        
        self.extra_details=self.page.find("section",{"data-testid":"Details"}).find("div",{"data-testid":"title-details-section"})  
        self.detail_parts=self.extra_details.find_all("li",class_="ipc-metadata-list__item") #finds all details parts
        for self.each_part in self.detail_parts:
            try: #this try/except finds labels of parts except IMDBPro.some labels are in "a" tag and some in "span" tag
                self.part_label=self.each_part.find("span",class_="ipc-metadata-list-item__label").text
            except:
                if not "companycredits" in self.each_part["data-testid"]:
                    self.part_label=self.each_part.find("a",class_="ipc-metadata-list-item__label ipc-metadata-list-item__label--link").text
            

            self.find_content=self.each_part.find("div",class_="ipc-metadata-list-item__content-container") #finds the content part of movie
            try :#this try/except finds the content of parts.some contents are in "a" tag and some in "span" tag
                if self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item") : 
                    self.part_content=[self.each_one.text for self.each_one in  self.find_content.find_all("span",class_="ipc-metadata-list-item__list-content-item")]

                else :
                    self.part_content=[self.each_one.text for self.each_one in self.find_content.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
            except:
                continue
            self.detail_dict[self.part_label]=self.part_content
            
        return self.detail_dict