from django.urls import path
from . import views

urlpatterns = [
    path('bfhl/post', views.bfhl_post, name='bfhl_post'),  # Use a different URL for POST
    path('bfhl/get', views.bfhl_get, name='bfhl_get'),    # Use a different URL for GET
]
