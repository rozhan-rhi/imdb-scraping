from total_directories.filter_search.movies_based_information import Filters,Movies

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