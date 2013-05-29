from django.db import models

# Create your models here.

class Game(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	age_limit = models.IntegerField(default=18)


	def __unicode__(self):
		return self.name

class GameDescription(models.Model):
	game = models.ForeignKey(Game)
	description = models.CharField(max_length=500)

	gen_RPG = 'RPG'
	gen_MMO = 'MMO'
	gen_ACT = 'ACT'
	gen_STRAT = 'STRAT'
	gen_RTS = 'RTS'

	GENRE_CHOICES = (
		(gen_RPG, 'RolePlayingGame'),
		(gen_MMO, 'MassiveMultiplayerOnline'),
		(gen_ACT, 'Action'),
		(gen_STRAT, 'Strategy'),
		(gen_RTS, 'RealTimeStrategy'),
	)

	genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default= gen_RPG)


	def __unicode__(self):
		return self.description


class GameReview(models.Model):
	game = models.ForeignKey(Game)
	reviewDescription = models.CharField(max_length=500, default= '')
	reviewTitle = models.CharField(max_length=100, default= '')

	def __unicode__(self):
		return self.reviewTitle

class GameRating(models.Model):
	gameReview = models.ForeignKey(GameReview)
	rating = models.IntegerField(default=3)

	def __unicode__(self):
		return str(self.rating)
		# Note:: This will cause errors if left as an int because unicode conversion expects string