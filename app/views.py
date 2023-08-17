from django.shortcuts import render, redirect, get_object_or_404
from . models import category, post, advert, comment, AddVideo
from . forms import PostForm, CatForm, contactForm, ads_fileForm, commentForm, AddVideoForm


def index(request):
    all_posts = post.objects.all()
    if all_posts:
        first_post = all_posts.last()
        if len(all_posts) >= 2:
            second_post = all_posts[len(all_posts) - 2]
        else:
            second_post = None
        if len(all_posts) >= 3:
            third_post = all_posts[len(all_posts) - 3]
        else:
            third_post = None
    else:
        first_post = None
        second_post = None
        third_post = None
    adverts=advert.objects.all()
    next_four_posts = all_posts[3:7]
    politics_posts = post.objects.filter(post_category__category_name='Politics').order_by('-date')[:4]
    last_five_videos = AddVideo.objects.all().order_by('-date')[:5]
    entertainment_videos = post.objects.filter(post_category__category_name='Entertainment').order_by('-date')[:5]
    cat = category.objects.all()

    return render(request, 'index.html', {
        'cat':cat,
        'first_post': first_post,
        'second_post': second_post,
        'third_post': third_post,
        'adverts':adverts,
        'next_four_posts': next_four_posts,
        'entertainment_posts': politics_posts,
        'last_five_videos': last_five_videos,
        'first_five_politics_videos': entertainment_videos,
    })





def bases(request):
    cats = category.objects.all()
    return render(request, 'base.html', {        'cats': cats
})


def each_category(request, pk):
    each_cat = get_object_or_404(category, pk=pk)
    posts_under_category = post.objects.filter(post_category=each_cat)
    return render(request, 'categori.html', {'each_cat': each_cat, 'posts_under_category': posts_under_category})


def ads_form(request):
    if request.method == 'POST':
        form = ads_fileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'post_list' with the URL name for the page where you list all posts
    else:
        form = ads_fileForm()
    return render(request, 'ads_form.html',{'form':form})



from django.db.models import Count
from django.db.models import F

def details(request, pk):
    post_object = get_object_or_404(post, pk=pk)
    cats = category.objects.all()
    cats_with_count = category.objects.annotate(total_posts=Count('post'))
    first_four_posts = post.objects.all()[:4]
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            new_comment = comment(posts=post_object, name=name, email=email, message=message)
            new_comment.save()
            return redirect('index')  # Replace 'index' with the URL name for the page where you want to redirect after submitting the comment
    else:
        form = commentForm()
    comments = comment.objects.filter(posts=post_object) 
    return render(request, 'blog_details.html', {
        'post_object': post_object,
        'form': form,
        'posts': post_object,
        'category': cats,
        'cats_with_count': cats_with_count,
        'first_four_posts': first_four_posts,
        'comments': comments,
    })


from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


    


from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def categories(request):
    return render(request, 'categori.html')

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Replace 'post_list' with the URL name for the page where you list all posts
    else:
        form = contactForm()
    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html')

def videos(request):
    video =AddVideo.objects.all()
    return render(request, 'videos.html',{'video':video})


from django.shortcuts import render
from django.db.models import Q
from .models import post

def manage(request):
    query = request.GET.get('q')
    if query:
        all_posts = post.objects.filter(title__icontains=query)
    else:
        all_posts = post.objects.all()
    return render(request, 'manage.html', {'all_posts': all_posts})





def update_post(request, pk):
    post_object = get_object_or_404(post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_object)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Replace 'post_list' with the URL name for the page where you list all posts
    else:
        form = PostForm(instance=post_object)

    return render(request, 'update.html', {'form': form, 'post_object': post_object})

def delete_post(request, pk):
    post_obj = get_object_or_404(post, pk=pk)

    if request.method == 'POST':
        post_obj.delete()
        return redirect('manage')  

    return render(request, 'delete.html', {'post': post_obj})


def add_category(request):
    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_category')  # Replace 'post_list' with the URL name for the page where you list all posts
    else:
        form = CatForm()
    return render(request, 'add_category.html',{'form':form})


def add_post(request):
    cat = category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'post_list' with the URL name for the page where you list all posts
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form, 'cat':cat})


def add_video(request):
    if request.method == 'POST':
        form = AddVideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos')  # Replace 'video_list' with the URL name for the page where you list all videos
    else:
        form = AddVideoForm()
    return render(request, 'add_video.html', {'form': form})















