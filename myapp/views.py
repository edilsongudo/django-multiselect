from django.shortcuts import render, redirect
from .forms import MyForm


# Create your views here.
def index(request):
	return render(request, 'myapp/index.html')


def select(request):
	if request.method == 'POST':
		# This prints to the console the post data
		print(request.POST)
		return redirect('index')