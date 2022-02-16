from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from profiles.serializers.profile_serializer import ProfileSerializer
from profiles.models import Profile


class ProfileView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    # parsers for supporting multipart HTML form content and file uploads
    parser_classes = [MultiPartParser, FormParser]
    http_method_names = ['patch']

    def get_object(self):
        return self.request.user.profile

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user)
