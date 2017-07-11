""" This module generates the HTML for the static web pages using the
    movie and list information passed into the open_movies_page() function """

import webbrowser
import os
import re


# Beginning head including stylesheets
MAIN_PAGE_HEAD = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="style.css">
'''


# Head of page continued with scripting for the page
MAIN_PAGE_SCRIPT = '''
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="page-header">
        <h1>{list_title} <small>by <a href="http://www.themoviedb.org/u/{list_author}">{list_author}</a></small></h1>
        {description}
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <div class="container">
      <div class="col-lg-12">
          <div class="footer">
            <a href="https://www.themoviedb.org"><img src="https://www.themoviedb.org/assets/static_cache/bb45549239e25f1770d5f76727bcd7c0/images/v4/logos/408x161-powered-by-rectangle-blue.png" alt="Powered by TMDb"></a>
            <br />
            <p>This product uses the TMDb API but is not endorsed or certified by TMDb.</p>
          </div>
      </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
MOVIE_TILE_CONTENT = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" class="poster" height="220">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    """ Creates a movile tile div for each movie using the movie
        and YouTube trailer information
    """

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )

    return content


def open_movies_page(movies, page_title, author, list_description):
    """ Generates HTML elements for each movie and compiles the HTML page
        into one """

    # filename of the output file constructed from page_title
    file_name = page_title.replace(" ", "_")

    # Create or overwrite the output file
    output_file = open(file_name + '.html', 'w')

    # replace title placeholder with page_title
    rendered_header = MAIN_PAGE_HEAD.format(title=page_title)

    # Replace the movie tiles placeholder generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies),
        list_title=page_title,
        list_author=author,
        description=list_description)

    # Output the file
    output_file.write(rendered_header + MAIN_PAGE_SCRIPT + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
