from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')

    data = []
    for n in notifications:
        data.append({
            'actor': n.actor.username,
            'verb': n.verb,
            'target': str(n.target),
            'timestamp': n.timestamp,
            'read': n.read,
        })

    return Response(data)
