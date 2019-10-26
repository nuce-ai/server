from ..model.models import Image
from . import serializers
from ..model import models
from rest_framework import generics, status
from rest_framework.response import Response

class ImageListView(generics.ListAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
class ImageCreateView(generics.CreateAPIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    def create(self, request, *args, **kwargs):

        super(ImageCreateView,self).create(request,args, kwargs)
        response = {
            "status_code" : status.HTTP_200_OK,
            "message"     : "Successfully created",
            "result"      : request.data,
        }
        return Response(response)
    