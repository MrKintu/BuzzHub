import os
from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures', null=True)
    id_document = models.ImageField(upload_to='id_documents', null=True,
                                    blank=True)
    doc_id = models.CharField(max_length=200, null=True, blank=True)
    d_o_b = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,
                                 blank=True)
    d_o_e = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,
                                 blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    favourite = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        full_path = self.id_document.file.name
        file_name = os.path.basename(full_path)
        return f'{file_name} - Profile'
