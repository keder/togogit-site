from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'notes'
urlpatterns = [
	# path('', views.index, name='index'),
	path('repositories', views.RepositoryListView.as_view(), name='repositories'),
	path('usernotes', views.NoteListView.as_view(), name='notes'),
	]
