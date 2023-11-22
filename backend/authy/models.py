import os
import string
from pathlib import Path
import random
from uuid import uuid4
from PIL import Image
# import Image
from django.contrib.auth.models import User
from django.db import models

from post.models import Post


def rename_id(instance, filename):
    ext = filename.split('.')[-1]
    rand_strings = ''.join(random.choice(string.ascii_lowercase + string.digits
                                         + string.ascii_uppercase)
                           for i in range(5))
    new_name = '{}{}.{}'.format(rand_strings, uuid4().hex, ext)

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    home = f'{BASE_DIR}/media/id_documents/{new_name}'
    new_path = os.path.join(home, new_name)

    return home


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', null=True,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_picture", null=True,
                              default="default.jpg")
    id_document = models.ImageField(upload_to=rename_id, null=True,
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

    # def __str__(self):
    #     return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
