class Human_Links :
    """includes all links"""
    def __init__(self,person_name=None,special_link=None) :
        self.person_url=f"https://www.imdb.com/search/name/?name={person_name}"
        self.bio_url=f"https://www.imdb.com{special_link}/bio?ref_=nm_ov_bio_sm"
        self.work_url=f"https://www.imdb.com{special_link}/?ref_=tt_ov_st"