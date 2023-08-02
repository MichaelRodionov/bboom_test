from django.urls import path

from . import views


# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('login/', views.login_view, name='user_login'),
    path('logout/', views.logout_view, name='user_logout'),
    path('posts/<int:pk>/', views.get_user_posts, name='user_posts'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('user_list/', views.get_list_users, name='user_list'),
]
