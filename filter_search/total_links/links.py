class Link_Base:
    """maintains all links"""
    
    def __init__(self,personal_link=None,rating_start=None,rating_end=None,movie_name=None,genre_name=None,date_start=None,date_end=None,adult_limit=None,country_name=None,opinion_part=None):
        self.main_page_url=f"https://www.imdb.com{personal_link}"
        self.rating_url=f"https://www.imdb.com/search/title/?user_rating={rating_start},{rating_end}&adult={adult_limit}"
        self.movie_name_url=f"https://www.imdb.com/search/title/?title={movie_name}"
        self.genre_url=f"https://www.imdb.com/search/title/?genres={genre_name}&adult={adult_limit}"
        self.release_url=f"https://www.imdb.com/search/title/?release_date={date_start},{date_end}&adult={adult_limit}"
        self.advanced_url="https://www.imdb.com/search/title/"
        self.country_url=f"https://www.imdb.com/search/title/?countries={country_name}&adult={adult_limit}"
        self.opinion_review=f"https://www.imdb.com{personal_link}reviews?ref_=tt_ql_sm"
        self.opinion_rating=f"https://www.imdb.com{personal_link}ratings?ref_=tt_ql_sm"
        self.tagline=f"https://www.imdb.com{tagline}taglines?ref_=tt_ql_sm"
        self.parent_guide=f"https://www.imdb.com{parent_guide}parentalguide?ref_=tt_ql_sm"
        self.awards_url=f"https://www.imdb.com{awards}awards?ref_=tt_ql_sm"