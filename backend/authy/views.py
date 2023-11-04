import json
import os
from pathlib import Path
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import resolve
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

from authy.models import Profile
from post.models import Post, Follow, Stream
from .forms import EditProfileForm, UserRegisterForm
from .BlobHandler import get_files, upload

load_dotenv()
env = os.environ


def UserProfile(request, username):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    posts = Post.objects.filter(user=user).order_by('-posted')

    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        posts = profile.favourite.all()

    # Profile Stats
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()
    # count_comment = Comment.objects.filter(post=posts).count()
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    # pagination
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'profile': profile,
        'posts_count': posts_count,
        'following_count': following_count,
        'followers_count': followers_count,
        'posts_paginator': posts_paginator,
        'follow_status': follow_status,
        # 'count_comment':count_comment,
    }
    return render(request, 'profile.html', context)


def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.image = form.cleaned_data.get('image')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile', profile.user.username)
    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'form': form,
    }
    return render(request, 'editprofile.html', context)


def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following, user=request.user).all().delete()
        else:
            posts = Post.objects.all().filter(user=following)[:25]
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=request.user, date=post.posted, following=following)
                    stream.save()
        return HttpResponseRedirect(reverse('profile', args=[username]))

    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))


@csrf_exempt
def register(request):
    response = ''
    if request.method == "POST":
        send = {
            'label': 'This POST was successful.'
        }
        response = json.dumps(send)
    else:
        send = {
            'label': 'This GET was successful.'
        }
        response = json.dumps(send)

    return HttpResponse(response)


def upload_passport(request):
    if request.method == "GET":
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        id_docs = get_files(f'{BASE_DIR}\\media\\id_documents')
        container = env.get('USER_ID_CONTAINER')
        status = upload(id_docs, container)

        response = ''
        if status:
            response = 'Uploaded Successfully.'
        else:
            response = 'Upload failed.'

        return HttpResponse(response)
