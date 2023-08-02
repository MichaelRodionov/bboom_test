from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from posts.models import Post
from ui.forms import UserLoginForm, PostForm
from users.models import User


# ----------------------------------------------------------------
def login_view(request):
    """
    View to 'login' user in application made by django form

    Params:
        - request: defines current request

    Returns:
        - redirect for user_post in case of successful login
        - render login page in case of not successful login
    """
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_posts', pk=user.pk)
    else:
        form = UserLoginForm(request)
    return render(request, 'users/login.html', {'form': form})


# ----------------------------------------------------------------
def logout_view(request):
    """
    View to 'logout' user

    Params:
        - request: defines current request

    Returns:
        - redirect to user_login page
    """
    logout(request)
    return redirect('user_login')


# ----------------------------------------------------------------
def get_list_users(request):
    """
    View to get list of all users

    Params:
        - request: defines current request

    Returns:
        - redirect to page with list of all users
    """
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})


# ----------------------------------------------------------------
def get_user_posts(request, pk):
    """
    View to get all posts by user (filter by pk)

    Params:
        - request: defines current request
        - pk: integer defines primary key of user

    Returns:
        - redirect to page with all posts of user
    """
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(user=user)
    return render(request, 'posts/posts.html', {'posts': posts, 'user': user, 'req_user_pk': request.user.pk})


# ----------------------------------------------------------------
@login_required
def add_post(request):
    """
    View to add new post. User must be authenticated to add post(!). Made by django form

    Params:
        - request: defines current request

    Returns:
        - redirect to page with all posts of user in case of successful result
        - render add post page in case of not successful result
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('user_posts', pk=request.user.pk)
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


# ----------------------------------------------------------------
@login_required
def delete_post(request, pk):
    """
    View to delete chosen post

    Params:
        - request: defines current request
        - pk: integer defines post primary key

    Returns:
        - redirect to page with list of all users
    """
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('user_posts', pk=request.user.pk)
