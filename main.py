# import filter_search
from filter_search import movies_based_information
from filter_search import information


obj=movies_based_information.Save_Info("https://www.imdb.com/search/title/?genres=crime")
# obj2=information.Filter_Base()
obj.calling_classes()
print(obj())



# obj=information.User_Reviews("https://www.imdb.com/search/title/?genres=drama")
# obj()
# print(obj.__str__())


    