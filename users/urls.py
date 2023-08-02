from django.urls import path

from users.views import UserRegView, UserListView, UserAuthView

# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('reg/', UserRegView.as_view()),
    path('auth/', UserAuthView.as_view()),
    path('list/', UserListView.as_view()),
]
