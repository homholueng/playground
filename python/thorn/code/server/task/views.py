import json
from uuid import uuid4

from django.shortcuts import render
from django.http.response import JsonResponse

from task import events


def fire_task_finished(request):
    events.task_finished.send({
        'id': uuid4().hex,
        'business_id': 13,
        'business_name': 'amazing business',
        'task_id': 2,
        'task_name': 'amazing task'
    })
    return JsonResponse({
        'result': True
    })

def subscribe_event(request):
    data = json.loads(request.body)
    
    sub