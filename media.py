import webbrowser


# main class which takes 5 arguements
class Movie():

    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# plays movie trailers in a webbrowser
    def show_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
