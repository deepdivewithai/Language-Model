from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('model.urls', namespace='models')),
    path('chat/', include('model2.urls', namespace='model2'))
]
