from django.shortcuts import render,redirect
from .models import Blog
from .forms import RegisterForm,ProfileForm,LoginForm,BlogForm
from django.contrib import auth

def index(request):
    return render(request,'myapp/index.html')

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return  render(request,'myapp/register.html',{'form':form})

def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        form = ProfileForm(instance=request.user.profile)
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
        return render(request,'myapp/profile.html',{'form':form,'current_user':current_user})
    else:
        return redirect('register')

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                print('enter')
                return redirect('blog')
    return render(request,'myapp/login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return render(request,'myapp/logout.html')

def blog_write(request):
    form = BlogForm()
    current_user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = request.POST.get('blog')
            post_blog = request.user.blog_set.create(blog=blog)
            post_blog.save()
            return redirect('myblog')
    return render(request,'myapp/blog_write.html',{'form':form,'user':current_user})

def myblog(request):
    current_user = request.user
    blogs = current_user.blog_set.all()
    return render(request,'myapp/myblog.html',{'blogs':blogs})

def blog_update(request,pk):
    sel_blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=sel_blog)
    if request.method == "POST":
        form = BlogForm(request.POST,instance=sel_blog)
        if form.is_valid():
            form.save()
            return redirect('myblog')
    return render(request,'myapp/blog_update.html',{'form':form})

def blog_delete(request,pk):
    sel_blog = Blog.objects.get(id=pk)
    sel_blog.delete()
    return redirect('myblog')
    
def blog(request):
    blogs = Blog.objects.all()
    return render(request,'myapp/blog.html',{'blogs':blogs})