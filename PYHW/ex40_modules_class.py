#dict style
#mystuff['apple']

#module style
#import mystuff #(mystuff.py)
#mystuff.apple()
#print mystuff.tangerine

#class style
#thing = MyStuff() #instantiate thing
#thing.apple()
#print thing.tangerine


class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally 'round the family", "With a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
