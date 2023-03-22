from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('owo/', include('task.urls')),
    path('admin/', admin.site.urls),
]
