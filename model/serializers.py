from rest_framework import serializers
from .models import Text

class TextSerializers(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('text',)