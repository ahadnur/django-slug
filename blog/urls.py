from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug_text>', views.post_detail, name='post_detail')
]
