class Song(object):

    def _init_(self,lyrics):
       self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
                   "I want to have some candies",
                   "So I'll ask for it from dada."])

bulls_on_parade = Song(["They really love to annoy me",
                        "with pocket full of candies still deny to give them to me."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
