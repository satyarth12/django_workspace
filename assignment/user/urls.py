from django.urls import path, include

from rest_framework import routers

from user.views.auth_views import RegisterView, LoginView, LogoutView
from user.views.user_views import UserView

app_name = "user"


router = routers.DefaultRouter()
router.register(r'user-detail', UserView, basename='user-detail')

urlpatterns = [
    path('register/', RegisterView.as_view(),
         name="register"),
    path('login/', LoginView.as_view(),
         name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', include(router.urls)),

]
