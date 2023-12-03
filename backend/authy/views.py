import json
import os
from pathlib import Path

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import resolve
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

from authy.models import Profile
from post.models import Post, Follow, Stream
from .BlobHandler import get_files, upload, container_files, file_urls
from .DocHandler import analyse_ID, PDFtoImage
from .FaceHandler import detect_face, TakeImages, TrainImages, TrackImages

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
        id_docs = get_files(f'{BASE_DIR}\\media\\id_documents')
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
    response = True

    return HttpResponse(response)


@csrf_exempt
@login_required
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


@csrf_exempt
@login_required
def FaceTraining(request):
    response = False
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        take_images = TakeImages(name)
        if take_images:
            train_images = TrainImages()
            if train_images:
                response = True

    return HttpResponse(response)


@csrf_exempt
@login_required
def TrackFace(request):
    response = False
    track_images = TrackImages()
    if track_images:
        response = True

    return HttpResponse(response)


@csrf_exempt
@login_required
def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    favs = profile.favourite.all()
    fav_list = []
    for x in range(len(favs)):
        single = favs[x]
        send = {
            'id': single.id,
            'picture': single.picture,
            'caption': single.caption,
            'posted': str(single.posted),
            'tags': str(single.tags),
            'user': str(single.user.username),
            'likes': single.likes
        }
        fav_list.append(send)
    profile_dict = {
        'user': profile.user.username,
        'doc_id': profile.doc_id,
        'd_o_b': str(profile.d_o_b),
        'd_o_e': str(profile.d_o_e),
        'bio': profile.bio,
        'location': profile.location,
        'country': profile.country,
        'url': profile.url,
        'favourites': fav_list
    }

    url_name = resolve(request.path).url_name
    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        posts = profile.favourite.all()
    posts_list = []
    for x in range(len(posts)):
        single = posts[x]
        send = {
            'id': single.id,
            'picture': single.picture,
            'caption': single.caption,
            'posted': str(single.posted),
            'tags': str(single.tags),
            'user': str(single.user),
            'likes': single.likes
        }
        posts_list.append(send)

    # Profile Stats
    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()
    # count_comment = Comment.objects.filter(post=posts).count()
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    context = {
        'posts': posts_list,
        'profile': profile_dict,
        'posts_count': int(posts_count),
        'following_count': int(following_count),
        'followers_count': int(followers_count),
        'follow_status': follow_status,
        # 'count_comment':count_comment,
    }
    response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def EditProfile(request):
    user = request.user

    if request.method == "POST":
        data = request.POST
        user_state = User.objects.get(username=user.username)
        profile_state = Profile.objects.get(user=user_state)

        user_state.username = data["username"]
        user_state.email = data["email"]
        user_state.save()

        profile_state.bio = data["bio"]
        profile_state.location = data["location"]
        profile_state.url = data["url"]
        profile_state.save()

        response = True
    else:
        user_state = User.objects.get(username=user.username)
        profile_state = Profile.objects.get(user=user_state)

        user_profile = {
            'username': str(user_state.username),
            'email': str(user_state.email),
            'first_name': str(user_state.first_name),
            'last_name': str(user_state.last_name),
            'd_o_b': str(profile_state.d_o_b),
            'bio': str(profile_state.bio),
            'location': str(profile_state.location),
            'country': str(profile_state.country),
            'url': str(profile_state.url)
        }
        response = json.dumps(user_profile)

    return HttpResponse(response)


@csrf_exempt
@login_required
def follow(request, username, option):
    user = request.user
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user,
                                                  following=following)

        if int(option) == 0:
            f.delete()
            (Stream.objects.filter(following=following, user=request.user).all()
             .delete())
        else:
            posts = Post.objects.all().filter(user=following)[:25]
            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=request.user, date=post.posted,
                                    following=following)
                    stream.save()
        response = True

        return HttpResponse(response)

    except User.DoesNotExist:
        response = False

        return HttpResponse(response)
