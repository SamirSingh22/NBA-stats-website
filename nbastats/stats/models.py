from django.db import models


class Player(models.Model):
	player_id = models.IntegerField()
	full_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=5)
	is_active = models.BooleanField()
	first_season = models.CharField(max_length=10)
	last_season = models.CharField(max_length=10)
	slug = models.SlugField()

	def __str__(self):
		return self.full_name


class Team(models.Model):
	team_id = models.IntegerField()
	team_name = models.CharField(max_length=50)
	team_abr = models.CharField(max_length=10)
	slug = models.SlugField()

	def __str__(self):
		return self.team_name


