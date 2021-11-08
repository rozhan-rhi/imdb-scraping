class Callback :
    def rating_callback(self,dict_,url=None) :
        pass

    def movie_name_callback(self,dict_,url=None):
        pass 

    def genre_callback(self,dict_,url=None):
        pass 

    def release_date_callback(self,dict_,url=None):
        pass 

    def country_callback(self,dict_,url=None):
        pass 



class Custom_Callback(Callback) :
    def rating_callback(self,dict_,url=None) :
        self.just_name_movies=dict_.keys()
        return self.just_name_movies

