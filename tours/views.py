from django.shortcuts import render
from tours.models import *
import json
from django.http import JsonResponse
from django.apps import apps
from django.db.utils import ConnectionDoesNotExist

# Create your views here.
def process_list(l1, l2):
    lst = [val for val in l1 if val in l2]
    return lst


def get_data(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        table_name = payload['data']['table_name'] if "tablename" in payload['data'] else payload['data']['worksheet_id'] if "worksheet_id" in payload['data'] else "NotGiven"
        select_list = [t['column'] for t in payload['data']['select_list']]
        column = [x.name for x in table1._meta.fields]
        c_list = process_list(select_list, column)
        Model = apps.get_model('tours', table_name)
        try:
            obj = Model.objects.using(payload['database_name']).all()
            if select_list is not None:
                data = []
            else:
                data = [s.get_info() for s in obj]
            return JsonResponse({'column': column, 'data': data})
        except ConnectionDoesNotExist:
            return JsonResponse({"message": 'Database Does Not exist'})
    else:
        return JsonResponse({"message": 'Not Valid Request'})

def fetch_details(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        return payload
