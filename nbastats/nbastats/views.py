from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request, 'base_layout.html')

def about(request):
	return render(request, 'base_layout.html')
