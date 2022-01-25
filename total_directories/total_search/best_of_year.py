from .t_links import T_Links
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re
from selenium.webdriver.common.by import By
from selenium import webdriver


class Bests:
    def common(self,url):
        self.parser="html.parser"
        self.req=requests.get(url)
        self.http_encoding = self.req.encoding if 'charset' in self.req.headers.get('content-type',"").lower() else None
        self.html_encoding = EncodingDetector.find_declared_encoding(self.req.content, is_html=True)
        self.encoding=self.http_encoding or self.html_encoding
        self.response=BeautifulSoup(self.req.content,self.parser,from_encoding=self.encoding)
        return self.response
    
    
    def find_bests(self,year):
        self.bests_of_year={}
        self.best_url=T_Links(year=year).best_of_year_url
        self.soup=self.common(self.best_url)            
        self.total_links=[]
        self.title=[]
        self.BST=[self.link for self.link in self.soup.find_all("a",href=True) if "/best-of/" in self.link["href"] and "/videoplayer/" not in self.link["href"]]
        for self.link in self.BST:
            try:
                self.t_movie=self.link.h3.text
                self.h_link=self.link["href"]
                if "/mediaviewer/" in self.h_link :
                    if re.findall("ls[0-9]+",self.h_link) :
                        self.title.append(self.t_movie)
                        self.id_=re.findall("ls[0-9]+",self.h_link).pop()
                        self.main_link=T_Links(id_=self.id_).if_best_link

                    elif re.findall("rg[0-9]+",self.h_link):
                        self.title.append(self.t_movie)
                        self.id_=re.findall("rg[0-9]+",self.h_link).pop()
                        self.main_link=T_Links(elif_id_=self.id_).elif_best_link
                    self.total_links.append(self.main_link)
                    
                else:
                    self.complete_url=T_Links(h_link=self.h_link).else_best_url
                    self.response=self.common(self.complete_url)
                    self.all_movie=self.response.find_all("div",class_="lister-item-content")
                    self.movies_name=[self.one.a.text for self.one in self.all_movie if re.findall("/title/tt[0-9]+", self.one.find("a",href=True)["href"])]
                    if len(self.movies_name)==0:
                        if re.findall("ls[0-9]+",self.h_link) :
                            self.title.append(self.t_movie)
                            self.id_=re.findall("ls[0-9]+",self.h_link).pop()
                            self.main_link=T_Links(h_listlink=self.id_).list_link
                        elif re.findall("rg[0-9]+",self.h_link):
                            self.title.append(self.t_movie)
                            self.id_=re.findall("rg[0-9]+",self.h_link).pop()
                            self.main_link=T_Links(h_gallerylink=self.id_).gallery_link
                                                  
                        self.total_links.append(self.main_link)
                    else: 
                        self.bests_of_year[self.t_movie]=self.movies_name
                
            except:
                pass
     


        self.TL=zip(self.title,self.total_links)
        self.browser=webdriver.Firefox()
        # self.browser.minimize_window()
        self.browser.implicitly_wait(20)
        for self.each_t,self.each_link in self.TL:
            self.m_soup=self.common(self.each_link)
            self.values=[]
            if re.findall("rg[0-9]+",self.each_link):
                self.rg=re.findall("rg[0-9]+",self.each_link).pop()
                self.pages=[self.item.strip() for self.item in self.m_soup.find("span",class_="page_list").text.strip().split("\n")]
                for self.page_num in self.pages:                
                    self.page_url=T_Links(rg=self.rg,page_num=int(self.page_num)).main_page_url
                    self.p_soup=self.common(self.page_url)
                    for self.each in self.p_soup.find_all("a",href=True) :
                        try:
                            if re.findall("rm([0-9]+)",self.each["href"]):
                                self.x=re.findall("rm([0-9]+)",self.each["href"]).pop()
                                self.m_link=self.each_link.split("/")
                                self.m_link[-1]="mediaviewer/"
                                self.movie_link="/".join(self.m_link)+f"rm{self.x}/"
                                self.browser.get(self.movie_link)
                                self.html=self.browser.find_element(By.CSS_SELECTOR,("a[class='ipc-md-link ipc-md-link--entity']"))
                                if not self.html.text in self.values:
                                    self.values.append(self.html.text)

                        except:pass

            else:
                for self.each in self.m_soup.find_all("a",href=True) :
                    try:
                        if re.findall("rm([0-9]+)",self.each["href"]):
                            self.x=re.findall("rm([0-9]+)",self.each["href"]).pop()
                            self.m_link=self.each_link.split("/")
                            self.m_link[-1]="mediaviewer/"
                            self.movie_link="/".join(self.m_link)+f"rm{self.x}/"
                            self.browser.get(self.movie_link)
                            self.html=self.browser.find_element(By.CSS_SELECTOR,("a[class='ipc-md-link']"))
                            if not self.html.text in self.values:
                                self.values.append(self.html.text)

                    except:pass
            self.bests_of_year[self.each_t]=self.values 
             
        self.browser.close()
        print(len(self.bests_of_year.keys()))
        return self.bests_of_year
                            

                

obj=Bests()
print(obj.find_bests(2021))
