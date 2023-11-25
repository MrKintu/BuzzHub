import json
import os
from pathlib import Path

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import resolve
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

from authy.models import Profile
from post.models import Post, Follow, Stream
from .BlobHandler import get_files, upload, container_files, file_urls
from .DocHandler import analyse_ID, PDFtoImage
from .FaceHandler import detect_face

load_dotenv()
env = os.environ


@csrf_exempt
def upload_ID(request):
    response = ''
    if request.method == "POST":
        newFile = request.FILES['NewFile']
        ext1 = newFile.name.split('.')[-1]
        good_ext = ['pdf', 'png', 'jpg', 'jpeg']
        if ext1 not in good_ext:
            response = ('Upload failed. Please upload in pdf, png, jpg or jpeg '
                        'format.')

        model = Profile()
        model.id_document = newFile
        model.save()
        state = Profile.objects.last()
        full_path = state.id_document.file.name
        file_name = os.path.basename(full_path)

        ext2 = file_name.split('.')[-1]
        profile = Profile.objects.get(pk=state.pk)
        if ext2 == 'pdf':
            imgPath = PDFtoImage(full_path)
            facePath = detect_face(imgPath)
            profile.image = facePath
        else:
            facePath = detect_face(full_path)
            profile.image = facePath
        profile.save()

        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        id_docs = get_files(f'{BASE_DIR}/media/id_documents')
        container = env.get('USER_ID_CONTAINER')
        blob_files = container_files(container)

        status = upload(container, id_docs, blob_files)
        if status:
            if file_name not in blob_files:
                file_url = file_urls(file_name, container)
                details = analyse_ID(file_url)
                send = {
                    'file_name': file_name,
                    'details': details
                }
                response = json.dumps(send)
        else:
            response = 'Upload failed.'

    return HttpResponse(response)


@csrf_exempt
def register(request):
    response = False
    if request.method == "POST":
        data = request.POST

        user = User.objects.create_user(
            username=data["username"],
            password=data["password"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"]
        )
        user.save()
        user_state = User.objects.get(username=data["username"])
        profile = Profile.objects.filter(
            id_document__endswith=data["file_name"])
        model = Profile.objects.get(pk=profile[0].pk)
        model.user = user_state
        model.doc_id = data["doc_id"]
        model.d_o_b = data["dob"]
        model.d_o_e = data["doe"]
        model.bio = data["bio"]
        model.location = data["location"]
        model.country = data["country"]
        model.save()

        response = True

    return HttpResponse(response)


@csrf_exempt
def login_view(request):
    response = False
    if request.method == "POST":
        data = request.POST
        username = data["username"]
        password = data["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = True
        else:
            response = False

    return HttpResponse(response)


@csrf_exempt
def logout_view(request):
    logout(request)


@csrf_exempt
def change_password(request):
    response = False
    if request.method == "POST":
        user = request.user
        data = request.POST

        if user.is_authenticated():
            user_state = User.objects.get(username=user.username)
            user_state.set_password(data["new_password"])
            user_state.save()

            response = True

    return HttpResponse(response)


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
    response = ''

    if request.method == "POST":
        pass
    else:
        pass

    return HttpResponse(response)


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
