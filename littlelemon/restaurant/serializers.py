from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu
from .models import Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name','price','inventory']

        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['first_name','last_name','guest_number','comment']


      #define Serializer class for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ['url', 'username', 'email', 'groups']  

