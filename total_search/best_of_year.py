from t_links import T_Links
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re
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
        self.best_url=T_Links(year=year).best_of_year_url
        self.soup=self.common(self.best_url)
        # self.all_parts=self.soup.find_all("div",class_="pagecontent")
        # self.total_links=[]
        # for self.part in self.all_parts:
        #     if self.part.find("div",id="main"):
        #         self.links= self.part.find_all("a",href=True)
        # for self.link in self.links:
        #     self.href_link=self.link["href"]
        #     if "best-of" in self.href_link.split("/"):
        #         if not "videoplayer" in self.href_link.split("/"):
        #             if not "?" in self.href_link.split("/")[2]:
        #                 self.complete_url="{}{}".format("https://www.imdb.com",self.href_link)
        #                 if not self.complete_url in self.total_links:
        #                     self.total_links.append(self.complete_url)
        # # return self.total_links
        # for self.best_part in self.total_links:
            # self.soup_part=self.common(self.best_part)
            # self.titles=[self.parts.a.text for self.parts in self.soup_part.find_all("div",class_="lister-item-content")]
            # if self.titles==[]:
            #     self.special_part=[self.part["href"] for self.part in self.soup_part.find_all("a",href=True) ]
            # #     # return self.special_part
            # #     # return self.best_part
            # # else: print(self.titles)
            # print(self.best_part)
            
            
        self.total_links=[]
        self.BST=[self.link["href"] for self.link in self.soup.find_all("a",href=True) if "/best-of/" in self.link["href"] and "/videoplayer/" not in self.link["href"]]
        for self.link in self.BST:
            if "/mediaviewer/" in self.link and re.findall("ls([0-9]+)",self.link):
                self.id_=re.findall("ls([0-9]+)",self.link).pop()
                self.main_link=f"https://www.imdb.com/list/ls{self.id_}/?ref_=ls_mv_sm"
                if not self.main_link in self.total_links:
                    self.total_links.append(self.main_link)
        
        for self.each_link in self.total_links:
            self.m_soup=self.common(self.each_link)
            for self.each in self.m_soup.find_all("a",href=True) :
                if re.findall("rm([0-9]+)",self.each["href"]):
                    self.x=re.findall("rm([0-9]+)",self.each["href"])
                    self.m_link=self.each_link.split("/")
                    self.m_link[-1]="mediaviewer/"
                    self.movie_link="/".join(self.m_link)+f"rm{self.x.pop()}/"
                    self.soup_movie=self.common(self.movie_link)
                    # if re.findall("/tt([0-9]+)/",self.soup_movie):
                    self.x=re.search('href="/title/tt([0-9]+)/',self.soup_movie.text)
                    return self.x
                    
                    # return type(self.soup_movie.text)
                    # self.x=[self.link["href"] for self.link in self.soup_movie.find_all("a") if re.findall("/tt([0-9]+)/",self.link["href"])]
                    # return self.x
                
                
                    # for self.one in self.x:
                    #     print(self.one)
                    #     if "/title/" in self.one["href"]:
                    # print(self.x)
                    # self.movie_name=[self.each_one["href"] for self.each_one in self.soup_movie.find_all("a",href=True) if "/title/" in self.each_one["href"]]
                    
                    
                    # self.open=self.common(self.x)
                    # self.y=self.soup_movie.find("a",href=True)
                    # return self.y
                
                
                
                # return self.each["href"]
            # self.special_part=[re.findall("rm([0-9]+)",self.each) for self.each in self.soup.find_all("a",href=True) if re.findall("rm([0-9]+)",self.each)]
            # return self.special_part
        
        
        # self.mlist=[]
        # self.best_url=T_Links(year=year).best_of_year_url
        # self.req=requests.get(self.best_url)
        # self.response=BeautifulSoup(self.req.text,"html.parser")    
        # self.best_parts=self.response.find("div",id="pagecontent").find("div",id="main").find_all("div",class_="article")
        # for self.each_part in self.best_parts:
        #     self.part_name=self.each_part.find("span",class_="oneline").a.text
        #     self.unique_part=self.each_part.find("p",class_="seemore").a["href"]
        #     self.second_url=T_Links(unique_part=self.unique_part).second_bests_url
        #     self.second_req=requests.get(self.second_url)
        #     self.second_response=BeautifulSoup(self.second_req.text,"html.parser")
            
        #     try:
        #         self.sections_of_apart=self.second_response.find("div",id="pagecontent")
        #         self.bests_of_apart=self.sections_of_apart.find("div",class_="article").find("div",class_="lister-list").find_all("div",class_="lister-item mode-detail")
        #         for self.each_one in self.bests_of_apart:
        #             self.title=self.each_one.find("div",class_="lister-item-content").h3.a.text.replace("\n","").strip()
        #             self.mlist.append(self.title)
        #         # print(self.mlist)
        #     except:
        #         self.all_parts=self.second_response.find("div",{"role":"presentation"}).find("div",{"data-testid":"action-bar"}).find("div",class_="styles__ActionWrapper-mtrg0k-3 ekFPqU")
        #         # .find("div",id="wrapper").find("div",id="content-2-wide")
        #         # .find("div",id="pagecontent")
        #         # .find("div",id="pagecontent").find("div",id="main").find("div",class_="article listo")
        #         return self.all_parts.prettify()
           
           
           
           
           
                

                
            # # for self.each_page in self.sections_of_apart:
            #     # try:
            # self.bests_of_apart=self.sections_of_apart[1].find("div",id="main").find("div",class_="article")
            # # .find("div",class_="article listo")
            # # .find("div",class_="lister-list").find_all("div",class_="lister-item mode-detail")
            # for self.each_one in self.bests_of_apart:
            #     self.title=self.each_one.find("div",class_="lister-item-content").h3.a.text
            #     self.mlist.append(self.title)
            #     # except:continue
            # return self.mlist
            #         # .find("div",class_="article listo").find("div",class_="article").find("div",class_="lister-list").find_all("div",class_="lister-item mode-detail")
            # # .find("div",class_="article listo")
            # # .find("div",class_="lister list detail sub-list").find("div",class_="lister-list").find_all("div",class_="lister-item mode-detail")
            # # for self.each_one in self.bests_of_apart:
            # #     self.title=self.each_one.find("div",class_="lister-item-content").h3.a.text
            # #     self.mlist.append(self.title)
            #         return self.bests_of_apart
            #     except:continue
obj=Bests()
print(obj.find_bests(2021))





# <div class="MediaSheetstyles__MainContentContainer-sc-1warcg6-5 VSwso"><div role="presentation" class="MediaSheetstyles__TitleContainer-sc-1warcg6-3 fjnjKY"><span>Top 10 Movies of 2021</span><span class="MediaSheetstyles__CountDisplay-sc-1warcg6-4 cUnOkd">2 of 10</span></div><div class="MediaSheetstyles__ContentContainer-sc-1warcg6-6 RCcIw"><div class="ipc-html-content ipc-html-content--baseAlt MediaSheetstyles__MainContent-sc-1warcg6-8 ctnkNW"><div><strong>9. <em><a class="ipc-md-link" href="/title/tt3228774/">Cruella</a></em> | Available to Stream on Disney Plus</strong><br><br>Early images of <a class="ipc-md-link" href="/name/nm1297015">Emma Stone</a> clad in couture and wrangling a pack of Dalmatians was all that was needed to spark excitement for this live-action Disney prequel. This Cruella de Vil origin story simultaneously released in theaters and on Disney Plus Premiere Access in May, hovering in the top 10 on MOVIEmeter for four weeks with Stone embodying the character of Estella — an ambitious, young fashionista debuting her punk-rock designs in 1970s London. The film won fans over by softening one of Disney's most wretched villains, and now we wait for Cruella's return — her second solo act is currently in pre-production.</div></div><div class="MediaSheetstyles__Divider-sc-1warcg6-9 fTPvhI"></div><div class="MediaSheetstyles__SecondaryContent-sc-1warcg6-10 hrbmLW"><div class="MediaSheetstyles__MetaSection-sc-1warcg6-14 EngQV"><span class="MediaSheetstyles__MetaTitle-sc-1warcg6-15 clrobR">People</span><span><a href="/name/nm1297015/?ref_=ls_mv" class="ipc-link ipc-link--baseAlt">Emma Stone</a>, <a href="/name/nm2181128/?ref_=ls_mv" class="ipc-link ipc-link--baseAlt">Joel Fry</a>, <a href="/name/nm3236159/?ref_=ls_mv" class="ipc-link ipc-link--baseAlt">Paul Walter Hauser</a></span></div><div data-testid="copyright"><div class="ipc-html-content ipc-html-content--baseAlt MediaSheetstyles__Copyright-sc-1warcg6-16 gQJNrG"><div>©&nbsp;2019 - Disney</div></div></div></div><div class="MediaSheetstyles__ActionBar-sc-1warcg6-11 cWDesb"></div></div></div>