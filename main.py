# import filter_search
from filter_search import movies_based_information
from filter_search import information


# obj=movies_based_information.Save_Info("https://www.imdb.com/search/title/?genres=crime")
# # # obj2=information.Filter_Base()
# obj.calling_classes()
# print(obj())



# obj=information.User_Reviews("https://www.imdb.com/search/title/?genres=drama")
# obj()
# print(obj.__str__())


# obj=movies_based_information.Movies()
# print(obj.several_movie("https://www.imdb.com/search/title/?genres=drama"))

obj=information.Awards("https://www.imdb.com/search/title/?genres=drama")
print(obj.awards_page())