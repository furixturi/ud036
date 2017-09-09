# -*- coding: utf-8 -*-
'''
title
storyline
poster_image_url
trailer_youtube_url

*self will be automatically added at instantiation
'''
import webbrowser

class Movie():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    # constructor, being called automatically at media.Motie(title, storyline, poster, trailer)
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method, self is automatically given 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
