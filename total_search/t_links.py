class T_Links:
    def __init__(self,month=None,day=None,year=None,unique_part=None):
        self.born_today_url=f"https://www.imdb.com/search/name/?birth_monthday={month}-{day}&ref_=nv_cel_brn"
        self.celeb_news_url="https://www.imdb.com/news/celebrity/?ref_=nv_cel_nw"
        self.best_of_year_url=f"https://www.imdb.com/best-of/?ref_=nv_ev_best_{year}"
        self.second_bests_url=f"https://www.imdb.com{unique_part}"