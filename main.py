from total_directories.filter_search.movies_based_information import Filters,Movies
from total_directories.total_search import Celeb_New,Born_Today,Prizes,What_To_Watch
from total_directories.human_search.filters import Actor_Info
# from imdbscraping.human_search.filters import *
# import pandas as pd

# obj=Filters()
# y=obj.country_filter("afghanistan")
# print(y)
# data=pd.DataFrame(y)
# data.to_csv("country_file.csv")



# x=obj.movie_name_filter("Buddha Collapsed Out of Shame")
# data=pd.DataFrame(x)
# data.to_csv("save_file.csv")
# print(x)


obj=Movies()
print(obj.several_movie("https://www.imdb.com/search/title/?genres=comedy"))
# print(obj.one_movie("https://www.imdb.com/search/title/?title=don't look up"))


# obj=Born_Today()
# print(obj.get_day_month())


# obj=Actor_Info("brad pitt","actor")
# print(obj())
