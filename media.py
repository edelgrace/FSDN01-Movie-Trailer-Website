""" This module contains classes involving the media movies """

import webbrowser


class Movie():
    """ This class stores information about movies

        Attributes:
                title (str): The movie title
                storyline (str): A brief overview of the movie storyline
                poster (str): URL to the path of movie poster image
                trailer (str): YouTube URL to the trailer video
    """

    def __init__(self, title, storyline, poster, trailer):
        """ The constructor will initialize the attributes of a movie instance
            using the given arguments

            Args:
                title (str): The movie title
                storyline (str): A brief overview of the movie storyline
                poster (str): URL to the path of movie poster image
                trailer (str): YouTube URL to the trailer video
        """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """ Opens a webrowser going to the YouTube trailer URL """

        webbrowser.open(self.trailer_youtube_url)
