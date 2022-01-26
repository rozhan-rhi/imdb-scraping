from total_directories.filter_search.movies_based_information import Filters,Movies
from total_directories.specific_search import Celeb_New,Born_Today,Prizes,What_To_Watch
from total_directories.human_search.filters import Actor_Info,Director_Info,Writer_Info
import pandas as pd
"""1.use this code to save information to save_file.csv     
        data=pd.DataFrame(data=obj.actor_bio())
        data.to_csv("save_file.csv")
        
    2.these are examples of working of some classes to know how to work with them"""
    
    

# obj=Filters()
# y=obj.country_filter("afghanistan")
# print(y)
# data=pd.DataFrame(y)
# data.to_csv("country_file.csv")


# x=obj.movie_name_filter("Buddha Collapsed Out of Shame")
# data=pd.DataFrame(x)
# data.to_csv("save_file.csv")
# print(x)


# obj=Movies()
# print(obj.several_movie("https://www.imdb.com/search/title/?genres=comedy"))
# obj2=obj.one_movie("https://www.imdb.com/search/title/?title=don't look up")
# df=pd.DataFrame(obj2)
# df.to_csv("save_information.csv")


# obj=Born_Today()
# print(obj.get_day_month())


# obj=Actor_Info("brad pitt","actor")
# data=pd.DataFrame(data=obj.actor_bio())
# data.to_csv("save_file.csv")


# obj=What_To_Watch()
# print(obj.guide())


# obj=Prizes()
# print(obj.center())
