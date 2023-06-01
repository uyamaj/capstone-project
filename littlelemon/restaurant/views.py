from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import views
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def index(request):
 return render(request, 'index.html', {})



class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet): 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

   
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 

    