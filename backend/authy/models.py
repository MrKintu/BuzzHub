import os
import random
import string
from pathlib import Path
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

from post.models import Post


def rename_id(instance, filename):
    ext = filename.split('.')[-1]
    rand_strings = ''.join(random.choice(string.ascii_lowercase + string.digits
                                         + string.ascii_uppercase)
                           for i in range(5))
    newname = '{}{}.{}'.format(rand_strings, uuid4().hex, ext)
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    new_path = f'{BASE_DIR}/media/id_documents/{newname}'

    return new_path


def rename_image(instance, filename):
    ext = filename.split('.')[-1]
    rand_strings = ''.join(random.choice(string.ascii_lowercase + string.digits
                                         + string.ascii_uppercase)
                           for i in range(5))
    newname = '{}{}.{}'.format(rand_strings, uuid4().hex, ext)
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    new_path = f'{BASE_DIR}/media/profile_pictures/{newname}'

    return new_path


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures', null=True)
    id_document = models.ImageField(upload_to='id_documents', null=True,
                                    blank=True)
    doc_id = models.CharField(max_length=200, null=True, blank=True)
    d_o_b = models.DateField(auto_now=False, auto_now_add=False, null=True,
                             blank=True)
    d_o_e = models.DateField(auto_now=False, auto_now_add=False, null=True,
                             blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    favourite = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.doc_id
