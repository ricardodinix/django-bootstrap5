from django.urls import path
from .views import home
from .views import post_detail

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/post_detail', post_detail, name='post_detail')

]