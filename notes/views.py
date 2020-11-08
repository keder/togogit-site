from django.shortcuts import render
from django.views.generic import ListView

from .models import Note, Repository


# def index(request):
# 	return render(request, 'index.html', {})


class NoteListView(ListView):
	model = Note


class RepositoryListView(ListView):
	model = Repository
