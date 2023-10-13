from django.shortcuts import render
from .models import Text
from .serializers import TextSerializers
from rest_framework.generics import CreateAPIView
from django.http import HttpResponse
from transformers import pipeline
import requests

class TextView(CreateAPIView):
    serializer_class = TextSerializers

    def post(self, request, *args, **kwargs):
        text = request.data.get('text', '')

        classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

        model_outputs = classifier([text])

        return HttpResponse(model_outputs[0], content_type='application/json')



