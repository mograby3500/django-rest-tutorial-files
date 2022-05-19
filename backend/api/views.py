import json

from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from products.models import *
from products.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance= serializer.save()
        print(serializer.data)
        return Response(serializer.data)
