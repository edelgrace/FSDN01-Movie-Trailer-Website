# TMDb Movie Trailer Website

This project generates a single page website in order to display movie trailers from any *public* list created on the website [The Movie Database (AKA TMDb)](http://themoviedb.org).

All this code is used for a project in Udacity's Full Stack Developer Nanodegree.

## Requirements

* [Python 3.6](https://www.python.org/downloads/)
* [requests](http://docs.python-requests.org/en/master/user/install/#install) module
* [API key](https://developers.themoviedb.org/3/getting-started) for The Movie DB

## How to Run

* [Install Python 3.6](https://www.python.org/downloads/) on your machine
* Install the requests module using pip ([tutorial](http://docs.python-requests.org/en/master/user/install/#install))

```
$ pip install requests
```

* Get an API key on [TMDb](https://themovedb.org) (register on their website and follow this [tutorial](https://developers.themoviedb.org/3/getting-started))
* Clone or download the source code of this repository
* Open a command line in the directory where all the files are located
* Run the following command:

```
$ python generate_pages.py [api-key]
```

This will open your default web browser to the generated web page. By default, the program will use one of my own lists on TMDb.

### Use Your Own Public TMDb List

```
$ python generate_pages.py [api-key] --list-id [list-id]
```

To find the list ID of a TMDb list, look at the URL of your list. For example, `http://www.themoviedb.org/list/[list-id]`.

## Limitations

* This will only retrieve the first page of your TMDb list

# Contact

Encountered any problems? Feel free to contact me!

* Twitter: [@edelgraceme](http://twitter.com/edelgraceme)
* E-mail: edel.altares@gmail.com
