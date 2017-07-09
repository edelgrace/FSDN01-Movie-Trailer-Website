""" This module generates all the class Movie instances and puts them in a list
    The movie list is then used to generate a web page to display as
    a website """

import fresh_tomatoes
import requests
import media
import argparse

def get_movie_list(args):
    """ This function pulls movies from a list on The Movie Database and
        creates Movie instances from the movies. The instances are then passed
        to a function to generate a web page
    """

    # initialize an empty list to store all movies
    movies = []

    print(args)
    
    # check if a list ID was specified at the command line
    if args is None:
        list_id = "27917"           # use the default list
    else:
        list_id = args   # use the list specified

    # using themoviedb.org API
    get_list = "https://api.themoviedb.org/4/list/"
    get_list += list_id 
    get_list += "?api_key=f99429863a7d560f97d2997d4b602460"

    # send request to API
    request = requests.get(get_list)

    # check if the response is OK (200 status code)
    if request.status_code != 200:
        # the list ID specified was not valid 
        print("The list ID " + list_id + " is not valid")
        
        # program exits
        return

    # convert the response to json format
    movie_list = request.json()

    # get the list details from the response
    description = movie_list['description']
    list_title = movie_list['name']
    list_author = movie_list['name']

    # process the list and put them into an array
    movies = process_movie_list(movie_list)

    #
    fresh_tomatoes.open_movies_page(movies, list_title, list_author, description)

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

        # retrieve the title depending on whether or not it is a movie or show
        if item['media_type'] == "movie":
            title = item['original_title']
        else:
            title = item['original_name']
        
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

    if "http://" not in trailer:
        trailer = "https://www.youtube.com/watch?v=D-CQVnuiR1I"

    return trailer


parser = argparse.ArgumentParser(description='Use your own TMdb list ID to generate a web page.')

parser.add_argument('--list-id', metavar='list_id', nargs='?', help='the list ID of the TMdb list')

args = parser.parse_args()

args = args.list_id

get_movie_list(args)
