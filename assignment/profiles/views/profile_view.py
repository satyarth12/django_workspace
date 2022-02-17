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

    def patch(self, request, *args, **kwargs):
        """Profile Update API
        """
        user = self.request.user
        data = request.data

        # making immutable dict to immutable
        new_data = data.copy()
        # adding user to data for seriazilzer
        new_data['user'] = user

        # getting the current user's profile obj
        profile_obj = self.get_object()

        serializer = self.serializer_class(
            instance=profile_obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # clearing m2m field
        profile_obj.team.clear()
        for i in data.get('profile_team').split(','):
            # adding the given team obj to m2m
            profile_obj.team.add(i)

        return Response(serializer.data)
