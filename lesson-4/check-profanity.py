# -*- coding: utf-8 -*-
import urllib

def read_text():
    quotes = open("./movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    result = connection.read()
    output = "Cannot examine the document."
    connection.close()
    
    if("true" in result):
        output = "Profanity Alert!"
    elif("false" in result):
        output = "No curse words found."
    
    print(output)

read_text()
