from .filter_basic import Filter_Base
from ..total_links import Link_Base
import re 

class Awards(Filter_Base) :
    """it has different methods to find movies' details"""
    
    def __init__(self,p_link):
        self.p_link=p_link
        
    def awards_page(self):
        self.award_dict={}
        self.page=Link_Base(awards=self.p_link).awards_url
        self.response=super().parse_page(self.page)
        self.all_awards_table=self.response.find_all("table",class_="awards")
        self.subject_table=[]
        
        
        self.no_content=self.response.find("div",id="no_content")
        if self.no_content!=None:
            self.extra=self.no_content.p.text
            self.content=self.no_content.text.replace(self.extra,"").strip()
            return self.content
        else:
            self.subject_table=[self.each_one.parent.text.strip() for self.each_one in self.response.find_all("a",href=True) if re.search("ev([0-9]+)",self.each_one["href"])] 
            for self.k,self.v in zip(self.subject_table,self.all_awards_table):
                self.award_key=self.k.replace("\n","")
                self.award_value=[self.each_td.text.replace("\n"," ") for self.each_td in self.v.find_all("td",class_="title_award_outcome")]
                self.award_dict[self.award_key]=self.award_value
            return self.award_dict