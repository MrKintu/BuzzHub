from PIL import Image
# import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from post.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pictures", null=True,
                              default="default.jpg")
    id_document = models.ImageField(upload_to="id_documents", null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    doc_id = models.CharField(max_length=200, null=True, blank=True)
    d_o_b = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,
                                 blank=True)
    d_o_e = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,
                                 blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    nation = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    favourite = models.ManyToManyField(Post, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
