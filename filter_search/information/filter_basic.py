import requests
from bs4 import BeautifulSoup
from total_links import Link_Base


class Filter_Base :
    """it has different methods to find movies' details"""

    def __str__(self):
        return f"the result of Filter_Base class is :\n{Filter_Base.movie_specs}"

    def parse_page(self,url) :
        """parse the url and save html text"""
        self.url=url
        self.response_=requests.get(self.url)
        self.parse=BeautifulSoup(self.response_.text,"html.parser")
        return self.parse
    
   

    def main_page(self,html_text) :
        """finds personal link of movie then goes to movie page and parses it"""
        self.movie_content=html_text
        self.personal_link=self.movie_content.h3.a["href"] #finds special url of movie
        self.new_page_movie=Link_Base(personal_link=self.personal_link).main_page_url #goes to movie page
        self.req_new_page=requests.get(self.new_page_movie)
        self.parse_new_page=BeautifulSoup(self.req_new_page.text,"html.parser")
        return self.parse_new_page
