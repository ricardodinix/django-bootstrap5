from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
