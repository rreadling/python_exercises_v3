class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# make a variable to pass to the class, this one is a list.
new_lyrics = ["I don't wanna work", "I wanna bang on the drum all day"]

# create an instance of Song with the variable as the argument
my_song = Song(new_lyrics)

# call on the mini-module to print your lyrics
my_song.sing_me_a_song()



