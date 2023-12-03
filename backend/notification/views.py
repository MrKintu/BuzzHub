import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from notification.models import Notification


@csrf_exempt
@login_required
def ShowNotification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    notice_list = []
    for x in range(len(notifications)):
        single = notifications[x]
        send = {
            'post': single.post.id,
            'sender': single.sender.username,
            'user': single.user.username,
            'notification_types': single.notification_types,
            'text_preview': single.text_preview,
            'date': str(single.date),
            'is_seen': single.is_seen
        }
        notice_list.append(send)

    context = {
        'notifications': notice_list,
    }
    response = json.dumps(context)

    return HttpResponse(response)


@csrf_exempt
@login_required
def DeleteNotification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    response = True

    return HttpResponse(response)
