import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from authy.models import Profile
from directs.models import Message


@csrf_exempt
@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None

    profile = get_object_or_404(Profile, user=user)

    direct_list = []
    message_list = []
    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user,
                                         reciepient=message['user'])
        directs.update(is_read=True)
        for x in range(len(directs)):
            single = directs[x]
            send = {
                'user': single.user.username,
                'sender': single.sender.username,
                'recipient': single.recipient.username,
                'body': single.body,
                'date': str(single.date),
                'is_read': single.is_read
            }
            direct_list.append(send)

        for x in range(len(messages)):
            single = messages[x]
            new_DM = single["last"]
            message_body = {
                'user': new_DM.user.username,
                'sender': new_DM.sender.username,
                'recipient': new_DM.recipient.username,
                'body': new_DM.body,
                'date': str(new_DM.date),
                'is_read': new_DM.is_read
            }
            send = {
                'recipient': single["user"].username,
                'message': message_body,
                'unread': single["unread"]
            }
            message_list.append(send)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'directs': direct_list,
        'messages': message_list,
        'active_direct': active_direct,
        'profile': profile.user.username,
    }
    response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def Directs(request, username):
    user = request.user
    active_direct = username
    messages = Message.get_message(user=user)

    directs = Message.objects.filter(user=user, recipient__username=username)
    directs.update(is_read=True)
    direct_list = []
    message_list = []
    for x in range(len(directs)):
        single = directs[x]
        send = {
            'user': single.user.username,
            'sender': single.sender.username,
            'recipient': single.recipient.username,
            'body': single.body,
            'date': str(single.date),
            'is_read': single.is_read
        }
        direct_list.append(send)

    for x in range(len(messages)):
        single = messages[x]
        new_DM = single["last"]
        message_body = {
            'user': new_DM.user.username,
            'sender': new_DM.sender.username,
            'recipient': new_DM.recipient.username,
            'body': new_DM.body,
            'date': str(new_DM.date),
            'is_read': new_DM.is_read
        }
        send = {
            'recipient': single["user"].username,
            'message': message_body,
            'unread': single["unread"]
        }
        message_list.append(send)

    for message in messages:
        if message['user'].username == username:
            message['unread'] = 0

    context = {
        'directs': direct_list,
        'messages': message_list,
        'active_direct': active_direct,
    }
    response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def SendDirect(request):
    response = False

    if request.method == "POST":
        data = request.POST
        from_user = request.user
        to_user_username = data["to_user"]
        body = data["body"]
        to_user = User.objects.get(username=to_user_username)
        Message.sender_message(from_user, to_user, body)
        response = True

    return HttpResponse(response)


@csrf_exempt
@login_required
def UserSearch(request):
    response = False

    if request == "POST":
        data = request.POST
        context = {}

        query = data["query"]
        users = User.objects.filter(Q(username__icontains=query))
        user_list = []
        for x in range(len(users)):
            single = users[x]
            send = {
                'username': single.username,
                'first_name': single.first_name,
                'last_name': single.last_name
            }
            user_list.append(send)
        context = {
            'users': user_list,
        }

        response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def NewConversation(request, username):
    from_user = request.user
    body = ''

    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        response = False
        return HttpResponse(response)
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    response = True
    return HttpResponse(response)
