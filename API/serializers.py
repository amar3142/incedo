from .models import Search_object
from rest_framework import serializers



class search_serializer(serializers.ModelSerializer):
    class Meta :
        model = Search_object
        fields = '__all__'
