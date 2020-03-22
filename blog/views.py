from django.shortcuts import render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,Createpost
from django.contrib.auth.models import User
from .models import Post
from django.contrib import messages
# Create your views here.
@login_required(login_url='/login')
def home(request):
    username = request.user.id
    queryset = Post.objects.filter(author=username).order_by('-created_on')
    template_name = "blogspost.html"
    return render(request,template_name,context={"posts" : queryset})
def post_detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,"single.html",context={"post": post})
# Create your views here.

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                next = request.GET['next']
            except:
                next="/"
            return redirect(next)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        myform = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            #user.refresh_from_db()
            #user.profile.mob = form.cleaned_data.get('mob')
            #user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            try:
                next = request.GET['next']
            except:
                next="/"
            return redirect(next)
        else:
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form,'myform': myform})
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def Logout(request):
    logout(request)
    return render(request,"logout.html")
def test(request):
    return render(request,"test.html")
def UsernameChecker(request):
    if request.method == 'POST':
        username = request.POST['user']
        if (User.objects.filter(username=username).exists()):
            return HttpResponse("not available")
        else:
            return HttpResponse("available")
    else:
        return HttpResponse("not allow")

@login_required(login_url='/login')
def createpost(request):
    if request.method=='POST':
        form = Createpost(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.author = request.user
            user.save()
            return redirect("/")
    form = Createpost()
    return render(request,"create.html", context={"form" : form})
def search(request):
    if request.method=='POST':
        username=request.POST['u']
        try:
            userid=User.objects.get(username=username).id
        except:
            return HttpResponse("User not found")
        queryset = Post.objects.filter(author=userid,status=0).order_by('-created_on')
        template_name = "blogspost.html"
        return render(request,template_name,context={"posts" : queryset})

    return render(request,"search.html")
        

