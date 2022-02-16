from django.urls import path
from user.views.auth_views import RegisterView, LoginView
from user.views.user_views import UserView

app_name = "user"

urlpatterns = [
    path('register/', RegisterView.as_view(),
         name="register"),
    path('login/', LoginView.as_view(),
         name="login"),
]
