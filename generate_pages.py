""" This module generates all the class Movie instances and puts them in a list.
    The movie list is then used to generate a web page to display as
    a website """

import fresh_tomatoes
import requests
import media

def get_movie_list():
    """ This function pulls movies from a list on The Movie Database and
        creates Movie instances from the movies. The instances are then passed
        to a function to generate a web page
    """

    # initialize an empty list to store all movies
    movies = []

    # using themoviedb.org API
    get_list = "https://api.themoviedb.org/4/list/27917?api_key=f99429863a7d560f97d2997d4b602460" # NOQA

    # send request to API
    request = requests.get(get_list)

    # convert the response to json format
    movie_list = request.json()

    # get the list description and list title from the response
    description = movie_list['description']
    list_title = movie_list['name']

    # process the list and put them into an array
    movies = process_movie_list(movie_list)

    #
    fresh_tomatoes.open_movies_page(movies, list_title, description)

    return

def process_movie_list(movie_list):
    """ This function goes through each movie in the pulled list from
        The Movie Database and creates an instance using the information
        provided from the API
    """

    # initialize an empty list to store all movies
    movies = []

    # get the list of all movies from the list
    movie_list = movie_list['results']

    # go through each movie in the list
    for item in movie_list:

        # retrieve the title
        title = item['original_title']

        # convert any special characters in the title to html entitities
        title = title.encode("ascii", "xmlcharrefreplace")
        title = title.decode("utf-8")

        # retrieve the storyline
        storyline = item['overview']

        # retrieve the path to the poster image
        img = "https://image.tmdb.org/t/p/w500" + item['poster_path']

        # retrieve the unique movie ID as defined on TMdb
        movie_id = item['id']

        # use the movie ID in order to find the trailer video
        trailer = get_trailer(movie_id)

        # make a new Movie instance
        movie_item = media.Movie(title, storyline, img, trailer)

        # add the movie to the movie list
        movies.append(movie_item)

    # return the list of movies processed
    return movies

def get_trailer(movie_id):
    """ This function grabs the YouTube trailer URL from the movie using
        a specific call to the API
    """

    # structure the URL for the API request
    url = "https://api.themoviedb.org/3/movie/"
    url += str(movie_id)  #
    url += "/videos?api_key=f99429863a7d560f97d2997d4b602460"

    trailer = requests.get(url)

    trailer = trailer.json()

    for video in trailer['results']:
        if video['site'] == "YouTube":
            trailer = "http://youtube.com/watch?v=" + video['key']
            break

    if not "http://" in trailer:
        trailer = "https://www.youtube.com/watch?v=D-CQVnuiR1I"

    return trailer

get_movie_list()
