
from django.shortcuts import render, redirect

#importเครื่องมือ
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import comment as Comments
from .forms import commentform

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def one(req):
	return render(req, 'myweb/one.html')

#def two(req):
   #return render(req, 'myweb/login.html')



def Register(req):
    return render(req, 'myweb/register.html')

def Login(req):
    return render(req, 'myweb/login.html')

def Rating(req):
    comments = Comments.objects.all()
    return render(req, 'myweb/rating.html',{'comments':comments})

def Register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f"New account created: {username}")
            login(req, user)
            return redirect("/index")

        else:
            for msg in form.error_messages:
                messages.error(req, f"{msg}: {form.error_messages[msg]}")

            return render(req,
                          template_name = "myweb/register.html",
                          context={"form":form})
    form = UserCreationForm(req.POST)
    return render(req,
                template_name = "myweb/register.html",
                context={"form":form})



def Login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.info(req, f"You are now logged in as {username}")
                return redirect('/index')
            else:
                messages.error(req, "Invalid username or password.")
        else:
            messages.error(req, "Invalid username or password.")
    form = AuthenticationForm()
    return render(req,
                  template_name = "myweb/login.html",
                  context={"form":form})

def logout(req):
    logout(req)
    messages.info(req, "Logged out successfully!")
    return redirect(" ")



def comment(request):
    if request.method == 'POST':
        form = commentform(request.POST)

        if form.is_valid():
            a = form.save()
            a.save()
            return redirect("/Rating")
    else:
        form = commentform()
        context = {'form': form}
        return render(request, 'myweb/comments.html', context)

