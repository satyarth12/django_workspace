from django.urls import path, include
from rest_framework import routers


from profiles.views.profile_view import ProfileView
from profiles.views.team_views import TeamView

app_name = "profiles"

router = routers.DefaultRouter()
router.register(r'team', TeamView, basename='team')

urlpatterns = [

    path('', include(router.urls)),

    path('update/', ProfileView.as_view(),
         name="profile-update"),
]
