from .filter_basic import Filter_Base
import re
class Movie_Participant(Filter_Base):
    """finds the name of the humans of movie"""
    
    def __init__(self,page) :
        self.page=page
        
        
    def people(self):
        self.people_dict={}
        self.info_parts=self.page.find_all("li",{"data-testid":"title-pc-principal-credit"}) #finds different parts of human table
        for self.each_one in self.info_parts:
            try: 
                self.info=self.each_one.span
                self.label_info=self.info.text
                self.content=[self.each_name.text for self.each_name in self.each_one.find_all("a",href=True) if "name" in self.each_name['href'].split("/")]
                self.people_dict[self.label_info]=self.content
                
            except:
                self.info=self.each_one.find("a",href=True)
                self.label_info=self.info.text 
                self.see_full_page=self.parse_page(f"https://www.imdb.com{self.info['href']}").find("table",class_="cast_list")
                self.all_options=list(filter(None,[self.name_movie.text.strip().replace("\n","") for self.name_movie in self.see_full_page.find_all("a",href=True) if "name" in self.name_movie['href'].split("/")]))
                self.content=self.all_options
                self.people_dict[self.label_info]=self.content
        return self.people_dict


            # else:
            #     self.info=self.each_one.span
            #     self.label_info=self.info.text
            #     self.content=[self.each_name.text for self.each_name in self.one.find_all("a",href=True) if "name" in self.each_name['href'].split("/")]
            #     self.people_dict[self.label_info]=self.content

        #     try:
        #         self.star_link=[self.one_star for self.one_star in self.each_one.find_all("a",href=True) if "fullcredits" in self.one_star['href'].split("/") ]
        #         self.star_link=''.join(self.star_link)
        #         if self.star_link.text.lower()=="stars":
        #             self.all_actor_link=f"https://www.imdb.com{self.star_link['href']}"
        #             self.actor_page=super().parse_page(self.all_actor_link)
        #             self.actors_table=self.actor_page.find("table",class_="cast_list")
        #             # for self.each_table in self.actors_table:
        #             # self.delete_options=[self.each_photo_link for self.each_photo in self.actors_table.find_all("td",class_="primary_photo")  for self.each_photo_link in self.each_photo.find_all("a")]
        #             self.all_options=[self.name_movie.text for self.name_movie in self.actors_table.find_all("a",href=True) if "name" in self.name_movie['href'].split("/")]

                    
        #             # for self.each_del_option in self.delete_options:
        #             #     self.all_options.remove(f"{self.each_del_option}")
        #     #         self.actors_names=self.all_options
        #     #     self.people_dict["actor"]="yes"
        #     # #             # if self.name not in self.actors_names:
        #     # #             #     self.actors_names.append(self.name.strip().replace("\n",""))
        #     # #         print(self.actors_names)

        #     except: 
        #         self.all_options="no"
        # self.people_dict["actor"]=self.all_options


                # self.actors_names=self.all_options

            # except:
            # else :
            #     self.actors_names=[self.item.text for self.item in self.each_one.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
        


        #     else:
        #         #finds the content of each part
        #         self.content_info=[self.item.text for self.item in self.each_one.find_all("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")]
        #         self.people_dict[self.label_info]=self.content_info
        # # except:pass
        
