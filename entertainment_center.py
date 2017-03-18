import media
import fresh_tomatoes

"""Creates an instance 'toy_story' using the Movie Class under media.py file
and provides values for each variable in __init__ function."""
toy_story = media.Movie(

    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

"""Creates an instance 'avatar' using the Movie Class under media.py file
and provides values for each variable in __init__ function."""

avatar = media.Movie(
    "Avator",
    "A story of a marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY&spfreload=10")

"""Creates an instance 'Ice_age_collision_course'
using the Movie Class under media.py file
and provides values for each variable in __init__ function."""

ice_age_collision_course = media.Movie(
    "Ice Age Collision Course",
    "Manny, Diego, and Sid join up with Buck to fend off""\n"
    "a meteor strike that would destroy the world.",
    "http://vignette4.wikia.nocookie.net/iceage/images/6/6f/Ice_Age_Collision_Course_Character_Posters_04.jpg/revision/latest?cb=20160317150324",  # nopep8
    "https://www.youtube.com/watch?v=Ohq6NmKMja8")

"""Creates an instance 'suicide_squad' using the Movie Class under media.py
file and provides values for each variable in __init__ function."""

suicide_squad = media.Movie(
    "Suicide Squad",
    "A task force of most dangerous people on the planet",
    "http://img12.deviantart.net/7a58/i/2016/232/3/0/suicide_squad_movie_poster_by_arkhamnatic-daeksy7.png",  # nopep8
    "https://www.youtube.com/watch?v=CmRih_VtVAs")

"""Creates an instance 'fearless' using the Movie Class under media.py file
and provides values for each variable in __init__ function."""

fearless = media.Movie(
    "Fearless",
    "a Chinese martial artist who challenged foreign""\n"
    "fighters in highly publicized events",
    "http://www.impawards.com/2006/posters/fearless_ver2.jpg",
    "https://www.youtube.com/watch?v=42NWMluhlfk")

"""Creates an instance 'shawshank_redemption' using the Movie Class under
media.py file and provides values for each variable in __init__ function."""

shawshank_redemption = media.Movie(
    "Shawshank Redemption",
    "tells the story of Andy Dufresne""\n"
    "A banker who is sentenced to life in Shawshank"
    "State Penitentiary for the murder of his wife and her love.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")

"""Creates an instance 'apocalypto' using the Movie Class under media.py file
and provides values for each variable in __init__ function."""

apocalypto = media.Movie(
    "Apocalypto",
    "The journey of a Mesoamerican tribesman who must""\n"
    "escape human sacrifice and rescue his family",
    "http://3.bp.blogspot.com/_lHqDPoQM38A/RjqAePruIsI/AAAAAAAAAAc/Wx5Sifmhvu0/s320/apocalypto+afiche.jpg",  # noqa
    "https://www.youtube.com/watch?v=ngWBddVNVZs")

"""Creates an instance 'the_dark_knight_rises' using the Movie Class
under media.py file and provides values for each variable
in __init__ function."""

the_dark_knight_rises = media.Movie(
    "The Dark Knight Rises",
    "Merciless revolutionary Bane forces an older Bruce Wayne save the city",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=GokKUqLcvD8")

"""Creates an instance 'dumb_and_dumber' using the Movie Class under media.py
file and provides values for each variable in __init__ function."""

dumb_and_dumber = media.Movie(
    "Dumb & Dumber",
    "Two unintelligent friends from Providence ""\n"
    "Rhode Island who set out on a cross-country trip",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
    "https://www.youtube.com/watch?v=l13yPhimE3o")

"""a list of movies inteances which used as an
arguement for fucntion 'open_movies_page' to generate
dynamic webpage using the fresh_tomatoes.py file"""

movies = [
    toy_story, avatar, ice_age_collision_course,
    suicide_squad, fearless, shawshank_redemption,
    apocalypto, the_dark_knight_rises, dumb_and_dumber]

fresh_tomatoes.open_movies_page(movies)
