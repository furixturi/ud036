'''
title
storyline
poster_image
trailer

*self will be automatically added at instantiation
'''
import webbrowser

class Movie():
    # constructor, being called automatically at media.Motie(title, storyline, poster, trailer)
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer = trailer_youtube

    # instance method, self is automatically given 
    def show_trailer(self):
        webbrowser.open(self.trailer)
