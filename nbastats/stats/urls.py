
from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', views.player_list),
	path('<slug>/', views.player_stats, name='player-stats')
]
