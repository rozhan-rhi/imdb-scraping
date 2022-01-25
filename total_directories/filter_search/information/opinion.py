from .filter_basic import Filter_Base
from ..total_links import Link_Base

class Awards(Filter_Base) :
    """it has different methods to find movies' details"""
    
    def __init__(self,p_link):
        self.p_link=p_link
        
    def awards_page(self):
        self.award_dict={}
        self.page=Link_Base(awards=self.p_link).awards_url
        self.response=super().parse_page(self.page)
        self.all_awards_table=self.response.find_all("table",class_="awards")
        try:
            self.subject_table=[]
            for self.each_one in self.response.find_all("h3"):
                if "/event/" in self.each_one.a["href"]:
                    self.subject_table.append(self.each_one.text.strip().replace("\n",""))
                    
            for self.k,self.v in zip(self.subject_table,self.all_awards_table):
                self.award_key=self.k
                self.award_value=[self.each_td.text.replace("\n"," ") for self.each_td in self.v.find_all("td",class_="title_award_outcome")]
                self.award_dict[self.award_key]=self.award_value
            return self.award_dict
        
        except:
            return "this movie doesn't have any awards"

        # except: pass
     
        # print(self.subject_table)

        # try:
        #     self.subject_table=[self.each_one for self.each_one in self.response.find_all("h3") if "event" in self.each_one.a["href"].split("/")]
        #     for self.k,self.v in zip(self.subject_table,self.all_awards_table):
        #         self.award_key=self.k.text.replace("\n","").strip()
        #         self.award_value=[self.each_td.text.replace("\n"," ") for self.each_td in self.v.find_all("td",class_="title_award_outcome")]
        #         self.award_dict[self.award_key]=self.award_value
        # # if not self.award_dict=={}:
        #         return self.award_dict
        # except:
        #     return "this movie doesn't have any awards"




    


