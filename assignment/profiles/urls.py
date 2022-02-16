from django.urls import path

from profiles.views.profile_view import ProfileView

app_name = "profiles"

urlpatterns = [
    path('update/', ProfileView.as_view(),
         name="profile-update"),
]
