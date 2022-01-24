import datetime
from t_links import T_Links 
from bs4 import BeautifulSoup
import requests
class Born_Today:
    def get_day_month(self):
        self.current_date=datetime.datetime.now()
        self.month=self.current_date.month
        self.day=self.current_date.day
        self.url=T_Links(month=self.month,day=self.day).born_today_url
        self.req=requests.get(self.url)
        self.response=BeautifulSoup(self.req.text,"html.parser")
        self.find_people=self.response.find("div",class_="lister-list").find_all("div",class_="lister-item mode-detail")
        self.people_name=[self.each_person.find("div",class_="lister-item-content").a.text.replace("\n","").strip() for self.each_person in self.find_people]
        return self.people_name
        
obj=Born_Today()
print(obj.get_day_month())