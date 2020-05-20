from django.db import models


class Player(models.Model):
	player_id = models.IntegerField()
	full_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=5)
	is_active = models.BooleanField()
	slug = models.SlugField()

	def __str__(self):
		return self.full_name

