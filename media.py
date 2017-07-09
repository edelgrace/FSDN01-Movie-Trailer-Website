""" This module contains classes involving the media movies """

import webbrowser

class Movie():
    """ This class stores movie information """

    def __init__(self, title, storyline, poster, trailer):
        """ The constructor will initialize the variables using the
            arguments provided
        """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """ Opens a webrowser going to the YouTube trailer URL """

        webbrowser.open(self.trailer_youtube_url)
