from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def one(req):
	return render(req, 'myweb/one.html')

