from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Search_object
from .serializers import search_serializer
# Create your views here.

class Query(APIView):
    def get(self,request):
        q = request.GET.get('q', None)
        if q:
            obj = Search_object.objects.filter(search_name__icontains=q)
            serialize = search_serializer(obj, many=True)
        return Response(serialize.data)
