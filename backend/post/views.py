import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from authy.models import Profile
from comment.models import Comment
from post.models import Post, Tag, Follow, Stream, Likes


@csrf_exempt
@login_required
def index(request):
    user = request.user
    all_users = User.objects.all()
    user_list = []
    for x in range(len(all_users)):
        single = all_users[x]
        send = {
            'username': single.username,
            'email': single.email,
            'first_name': single.first_name,
            'last_name': single.last_name
        }
        user_list.append(send)

    follow_status = (Follow.objects.filter(following=user, follower=request.user)
                     .exists())

    profile = Profile.objects.all()
    profile_list = []
    for x in range(len(profile)):
        single = profile[x]
        send = {
            'doc_id': single.doc_id,
            'd_o_b': str(single.d_o_b),
            'd_o_e': str(single.d_o_e),
            'bio': single.bio,
            'location': single.location,
            'country': single.country,
            'url': single.url
        }
        profile_list.append(send)

    posts = Stream.objects.filter(user=user)
    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)

    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    post_list = []
    for x in range(len(post_items)):
        single = post_items[x]
        send = {
            'id': single.id,
            'picture': single.picture,
            'caption': single.caption,
            'posted': str(single.posted),
            'tags': str(single.tags),
            'user': single.user.username,
            'likes': single.likes
        }
        post_list.append(send)

    query = request.GET.get('q')
    users_paginator = ''
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

    context = {
        'post_items': post_list,
        'follow_status': follow_status,
        'profile': profile_list,
        'all_users': user_list,
        'users_paginator': users_paginator,
    }
    response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def NewPost(request):
    response = False

    if request.method == "POST":
        user = request.user
        data = request.POST
        picture = request.FILES['image']
        caption = data["caption"]
        tag_form = data["tags"]
        tag_list = list(tag_form.split(','))

        tags_obj = []
        for tag in tag_list:
            t, created = Tag.objects.get_or_create(title=tag)
            tags_obj.append(t)
        p, created = Post.objects.get_or_create(picture=picture,
                                                caption=caption, user=user)
        p.tags.set(tags_obj)
        p.save()
        response = True

    return HttpResponse(response)


@csrf_exempt
@login_required
def PostDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_item = {
        'id': str(post.id),
        'picture': post.picture.file.name,
        'caption': post.caption,
        'posted': str(post.posted),
        'tags': str(post.tags),
        'user': post.user.username,
        'likes': post.likes
    }

    comments = Comment.objects.filter(post=post).order_by('-date')
    comment_list = []
    for x in range(len(comments)):
        single = comments[x]
        send = {
            'post': str(single.post.id),
            'user': single.user.username,
            'body': single.body,
            'date': str(single.date)
        }
        comment_list.append(send)

    context = {
        'post': post_item,
        'comments': comment_list
    }

    response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def Tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')
    posts_list = []
    for x in range(len(posts)):
        single = posts[x]
        send = {
            'id': single.id,
            'picture': single.picture,
            'caption': single.caption,
            'posted': str(single.posted),
            'tags': str(single.tags),
            'user': single.user.username,
            'likes': single.likes
        }
        posts_list.append(send)

    context = {
        'posts': posts_list,
        'tag': tag

    }
    response = json.dumps(context)

    return HttpResponse(response)


# Like function
@csrf_exempt
@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()
    response = True

    return HttpResponse(response)


@csrf_exempt
@login_required
def favourite(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)

    if profile.favourite.filter(id=post_id).exists():
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)
    response = True

    return HttpResponse(response)
