from django.shortcuts import get_object_or_404, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from photo.models import Photo


class AddToFavorite(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        photo = get_object_or_404(Photo, pk=pk)
        user = request.user
        if user in photo.favorite.all():
            photo.favorite.remove(user)
            photo.save()
            return Response({"favorite_info": "Removed from favorite"})
        else:
            photo.favorite.add(user)
            photo.save()
            return Response({"favorite_info": "Added to favorite"})
