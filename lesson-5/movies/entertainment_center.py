# -*- coding: utf-8 -*-
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#           file_name.class_name()
# Movie class's __init__ function gets called

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)
#avatar.show_trailer()


captain_america_3 = media.Movie("Captain America 3: Civil War",
                                "Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage. The new status quo deeply divides members of the team. Captain America (Chris Evans) believes superheroes should remain free to defend humanity without government interference. Iron Man (Robert Downey Jr.) sharply disagrees and supports oversight. As the debate escalates into an all-out feud, Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner) must pick a side.",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj",
                                "https://www.youtube.com/watch?v=1L3c17AmCZw")
#captain_america_3.show_trailer()

movies = [toy_story, avatar, captain_america_3]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.valid_ratings)
