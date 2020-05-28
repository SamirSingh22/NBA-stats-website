
from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('players/', views.player_list, name='players-stats'),
	path('', views.stats, name='stat-home'),
	path('players/<slug>/', views.player_profile, name='player-profile'),
	path('players/<slug>/career_stats/<per_mode>/', views.career_stats, name='career-stats'),
	path('teams/', views.team_list, name='teams')
]
