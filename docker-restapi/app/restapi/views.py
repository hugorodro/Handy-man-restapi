from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Order, Product_Order, Product, JobSite, Vendor
from .serializers import OrderSerializer, ProductOrderSerializer, ProductSerializer, VendorSerializer, JobSiteSerializer, UserSerializer 

# from .forms import OrderForm, MultipleOrderForm
from django.forms import formset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django_filters import rest_framework as filters

# import Template view Module
from django.views.generic.base import TemplateView 


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['id']

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(pk=token.user_id)
        return Response({
            'token': token.key, 
            'id': token.user_id,
            'first_name': user.first_name,
            'last_name': user.last_name
        })

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.DjangoFilterBackend]

    # def create(self, request):
    #     instance =self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
        
class ProductOrderView(viewsets.ModelViewSet):
    queryset = Product_Order.objects.all()
    serializer_class = ProductOrderSerializer
    filter_backends = [filters.DjangoFilterBackend]

class ProductOrderList(viewsets.ModelViewSet):
    queryset = Product_Order.objects.all()
    serializer_class = ProductOrderSerializer
    filter_backends = [filters.DjangoFilterBackend]


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]

class JobSiteView(viewsets.ModelViewSet):
    queryset = JobSite.objects.all()
    serializer_class = JobSiteSerializer
    filter_backends = [filters.DjangoFilterBackend]

 
class VendorView(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [filters.DjangoFilterBackend]



 
# html template views

class HomeView(TemplateView):
    template_name = "restapi/home.html"

class PrivacyView(TemplateView):
    template_name = "restapi/privacy_policy.html"

class TermsView(TemplateView):
    template_name = "restapi/terms_and_conditions.html"