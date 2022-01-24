from imdbscraping.filter_search.movies_based_information import Filters
from imdbscraping.human_search.filters import *
import pandas as pd

obj=Filters()
y=obj.country_filter("afghanistan")
data=pd.DataFrame(y)
data.to_csv("country_file.csv")



# x=obj.movie_name_filter("Buddha Collapsed Out of Shame")
# data=pd.DataFrame(x)
# data.to_csv("save_file.csv")
# print(x)