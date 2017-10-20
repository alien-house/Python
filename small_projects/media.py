import webbrowser
class Movie():
    """ This class  provides a way to store movie related information  """ 
    
    valid_ratings =  ["G", "PG", "PF-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, movie_imageurl, trailer_youtube):
        self.title  = movie_title
        self.storyline = movie_storyline
        self.poster_imageurl  = movie_imageurl
        self.traile_youtubeurl  = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.traile_youtubeurl)

