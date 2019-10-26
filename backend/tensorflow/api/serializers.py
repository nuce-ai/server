from ..model.models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('iid','content','label')