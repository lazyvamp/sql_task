from django.shortcuts import render
from tours.models import *
import json
from django.http import JsonResponse
from django.apps import apps
from django.db.utils import ConnectionDoesNotExist
from .parse import SqlParse

# Create your views here.
def get_data(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        import ipdb; ipdb.set_trace()
        SqlParse.select_all(payload['data'])
        table1.objects.using('hwll').raw("select * from ")
        return JsonResponse({"hell":"miss"})