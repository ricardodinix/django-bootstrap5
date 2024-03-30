from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from .views import post_detail

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/post_detail', post_detail, name='post_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)