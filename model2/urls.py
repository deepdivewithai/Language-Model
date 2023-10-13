from django.urls import path
from . import views

app_name = 'model2'

urlpatterns = [
    path('', views.TextView.as_view(), name='text')
]
