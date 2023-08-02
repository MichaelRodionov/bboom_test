from django.urls import path

from posts.views import PostCreateView, PostListView, PostDeleteView

# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('create/', PostCreateView.as_view()),
    path('list/', PostListView.as_view()),
    path('<int:pk>/', PostDeleteView.as_view()),
]
