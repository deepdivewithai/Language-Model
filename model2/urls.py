from django.urls import path
from . import views

app_name = 'model2'

urlpatterns = [
    path('', views.Chatbot.as_view(), name='chatbot')
]
