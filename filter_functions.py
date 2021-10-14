from filter_basic import Filter_Base
import requests
from links import Link_Base

class Filters_Sub(Filter_Base,Link_Base) :

    def common_part(self,func) :
        obj.parse_page(func)
        self.total_info=obj.several_movie(obj.main_page,obj.movie_detail)
        return self.total_info
    
    def rating_filter(self,start,end) :
        self.url=Link_Base(rating_start=start,rating_end=end).rating_url
        return obj.common_part(self.url)

    def movie_name_filter(self,name):
        self.url=Link_Base(movie_name=name).movie_name_url
        obj.parse_page(self.url)
        self.total_info=obj.one_movie(obj.main_page,obj.movie_detail)
        return self.total_info

    def genre_filter(self,genre_name):
        self.url=Link_Base(genre_name=genre_name).genre_url
        return obj.common_part(self.url)

    def release_date_filter(self,start,end):
        self.url=Link_Base(date_start=start,date_end=end).release_url
        return obj.common_part(self.url)


obj=Filters_Sub()
# obj_link=Link_Base()
# obj_filter_base=Filter_Base()
# print(obj.rating_filter("7","8"))
print(obj.release_date_filter("2020-01-01","2020-12-12"))

# x=obj.parse_page(obj.rating("7.0","7.8"))
# print(obj.several_movie(obj.main_page,obj.movie_detail))