from django.urls import path

from myapp.api.views import child

urlpatterns = [
    path('demo/<int:pk>', child, name='childs'),
]
