from rest_framework import generics
import openai
import os
from dotenv import load_dotenv
from .serializers import TextSerializers
from django.http import HttpResponse

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

class Chatbot(generics.CreateAPIView):
    serializer_class = TextSerializers

    def post(self, request, *args, **kwargs):
        text = request.data.get('text', '')
        chatbot_response = None

        if api_key is not None:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text},
                ],
            )
            
            chatbot_response = response['choices'][0]['message']['content']

        return HttpResponse(chatbot_response, content_type='application/json')
