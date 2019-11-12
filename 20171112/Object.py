class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_baby = Song(["Happy birthday to you", "I don`t want to get sued", "So I`ll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

a = Song(["I love you", "I`ll hope with you ever"])
a.sing_me_a_song()


import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {"class %%%(%%%):" : "Make a class named %%% that is-a %%%",
"class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** parameters."}