#fresh_tomatoes
create a movie trail html page

##installation
no need to nistall

##use of file
###README.md
help and introduction file

###fresh_tomatoes.html
this file is created by you computer which is the final result
you can open it by webbrowser to see how it is.

###fresh_tomatoes.py
this is the setting of output html you can quickly change the effect of generated web page

as an example
'''html

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="246" height="138">     #the value of width and height  are the value of your pictures' width and height in the web page
    <h2>{movie_title}</h2>
</div>
'''

###entertainment_center.py
here is an example of movie 
'''python
first = media.Movie("ALL SUPERHERO MOVIES 2017 Trailer",
                        "Here are all Superhero Movies 2017 with Trailer",
                        "https://i.ytimg.com/vi/0Szbs34k3-Y/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDsD2y5S1NCDNV1Urdq0jfy95DUBQ",
                        "https://www.youtube.com/watch?v=0Szbs34k3-Y")
'''


you can add you own movie by write code like
_movie_name_ = media.Movie(_movie_name_,_story_line_,_post_url_,_video_url_)
	ps: things with '_ _' need you to replace   like " _movie_name_ "  to "first"
	ps:_post_url_  , _video_url_  can be copied from youtube  think of it
	
and add "_movie_name_"  to movies array like
movies = [first,second,third,fourth,fifth,sixth,_movie_name_]

the save and run the python file then it will create a html file

###media.py
 file for pro
 
#end












