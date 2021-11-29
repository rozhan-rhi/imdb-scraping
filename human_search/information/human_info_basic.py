from bs4 import BeautifulSoup
import requests
import re
from .links_human import Human_Links
class Human_Basic:
    """find all information about a person who is an actor or director or writer"""

    def __init__(self,name) :
        self.name=name


    def common_parsing(self,url):
        """parse the url and return html text"""
        self.req=requests.get(url)
        self.parse=BeautifulSoup(self.req.text,"html.parser")
        return self.parse
    

    def personal_link(self):
        """find the special link of person"""
        self.url=Human_Links(person_name=self.name).person_url   #use person url of links_human ,search according to the name
        self.total_page=self.common_parsing(self.url)
        self.person_link=self.total_page.find("div",class_="lister-item-content").a["href"] #find special part of link
        return self.person_link

        
    
    def personal_bio(self) :
        """go to the personal page of person"""
        self.personal_link()
        self.url=Human_Links(special_link=self.person_link).bio_url   #use bio url of links_human 
        self.total_page=self.common_parsing(self.url)
        return self.total_page



    def overview(self):
        """find information about person itself"""
        self.overview_dict={}
        self.born_list=[]
        self.personal_bio()
        self.overview_part=self.parse.find("table",id="overviewTable").find_all("tr")   #finds different parts of overview table
        for self.each_part in self.overview_part :
            self.td_tags=self.each_part.find_all("td",class_="label")   #finds the titles of parts
            for self.each_td in self.td_tags: 
                if self.each_td.text.lower()=="born": #find born title 
                    self.time_place=self.each_part.find_all("a") #find the born place and date of birth of person
                    for self.one in self.time_place :
                        self.born_list.append(self.one.text)  
                    self.overview_dict["born"]=self.born_list

                else : #for titles except born
                    self.content=self.each_part.text.replace(self.each_td.text, "").replace("\n","")  #find the content of titles
                    self.overview_dict[self.each_td.text.lower()]=self.content.encode("ascii","ignore").decode("utf-8").strip()
        return self.overview_dict



    def family(self) :
        """finds information about the family of person"""
        self.family_dict={}
        self.personal_bio()
        try:
            
            self.family_part=self.parse.find("table",id="tableFamily").find_all("tr")   #finds different parts of family table
            for self.each_part in self.family_part :
                self.titles=self.each_part.find("td").text.strip() #finds the titles of parts
                if self.titles.lower()=="spouse" :  #finds spouse title
                    try:
                        self.a_tags=self.each_part.find_all("a")              
                        #finds the contents of tiltles by finding "a" tags that have name in their links
                        self.title_name=[self.each_href.text for self.each_href in self.a_tags if "name" in self.each_href["href"]]
                        self.family_dict["spouse"]=self.title_name
                    except:continue
                else : #for other titles except spouse
                    for self.item in self.each_part.find_all("td") :    #finds all titles with their contents
                        if self.titles not in self.item.text:   #seperate contents of titles
                            if self.item.text.strip()!=str(None):   #finds not None content
                                self.content=self.item.text.replace(" ","")
                                self.content=re.sub("\(.*?\)"  ,"",self.content).replace(" ","").split("\n") #remove information in parantheses & whitespaces from content
                                self.content=list(filter(None,self.content)) #final content of part
                                self.family_dict[self.titles]=self.content
            
            return self.family_dict 
        except:
            return "no family information"
        
    
    def salary(self):
        self.salary_dict={}
        self.salary_list=[]
        self.personal_bio()
        try:
            self.salary_part=self.parse.find("table",{"id":"salariesTable"}).find_all("tr")
            for self.each_one in  self.salary_part:
                self.label=self.each_one.a.text
                self.content_part=(self.each_one.text.replace("\n","").replace(self.label,"").strip().encode("ascii","ignore").decode("utf-8").split(" "))
                self.true_content=list(filter(None,self.content_part))
                self.salary_dict[self.label]=self.true_content
            return self.salary_dict 
        except:
            return "no salary information"
