# Movie Trailer Website

This project generates a single page website in order to display movie trailers from any *public* list created on the website [The Movie Database (AKA TMdb)](http://themoviedb.org).

All this code is used for a project in Udacity's Full Stack Developer Nanodegree.

## Requirements

* [Python 3.6](https://www.python.org/downloads/)
* [requests module](http://docs.python-requests.org/en/master/user/install/#install)
* A public list on TMdb that only contains movies!

## How to Run

* Clone or download the source code 
* Open a command line in the directory where all the files are located
* Run the following command:

```
$ python generate_pages.py
```

This will open your default web browser to the generated web page. By default, the program will use one of my own lists on TMdb.

### Use Your Own Public TMdb List

```
$ python generate_pages.py --list-id [list-id]
```

To find the list ID of a TMdb list, look at the URL of your list. For example, `http://www.themoviedb.org/list/[list-id]`.

If an invalid list ID is specified, then the program will exit.

# Contact

Encountered any problems? Feel free to contact me!

* Twitter: [@edelgraceme](http://twitter.com/edelgraceme)
* E-mail: edel.altares@gmail.com
