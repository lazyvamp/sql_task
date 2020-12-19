from django.shortcuts import render
from tours.models import *
import json
from django.http import JsonResponse
from django.apps import apps
from django.db.utils import ConnectionDoesNotExist
from .parse import sql_wrappr
from django.core import serializers

# Create your views here.
def get_data(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        database = payload['database_name']
        final_sql, column_names = sql_wrappr(payload['data'])
        Model = apps.get_model('tours', payload['data']['worksheet_id'])
        requested_data = Model.objects.using(database).raw(final_sql)
        import ipdb; ipdb.set_trace()
        return JsonResponse({"hell": requested_data})