class T_Links:
    def __init__(self,month=None,day=None,year=None,unique_part=None,id_=None,elif_id_=None,h_link=None,h_listlink=None,h_gallerylink=None,
                 rg=None,page_num=None,parent=None,group=None):
        self.born_today_url=f"https://www.imdb.com/search/name/?birth_monthday={month}-{day}&ref_=nv_cel_brn"
        self.celeb_news_url="https://www.imdb.com/news/celebrity/?ref_=nv_cel_nw"
        self.best_of_year_url=f"https://www.imdb.com/best-of/?ref_=nv_ev_best_{year}"
        self.second_bests_url=f"https://www.imdb.com{unique_part}"
        self.if_best_link=f"https://www.imdb.com/list/{id_}/?ref_=ls_mv_sm"
        self.elif_best_link=f"https://www.imdb.com/gallery/{elif_id_}/?ref_=rg_mv_sm"
        self.else_best_url=f"https://www.imdb.com/{h_link}"
        self.list_link=f"https://www.imdb.com/list/{h_listlink}/?ref_=ls_mv_sm"
        self.gallery_link=f"https://www.imdb.com/gallery/{h_gallerylink}/?ref_=rg_mv_sm"
        self.main_page_url=f"https://www.imdb.com/gallery/{rg}?page={page_num}&ref_=rgmi_mi_sm"
        self.guide_url="https://www.imdb.com/what-to-watch/?ref_=hm_watch_btn"
        self.second_guide_url=f"https://www.imdb.com{parent}"
        self.link_group=f"https://www.imdb.com/search/title/?groups={group}"