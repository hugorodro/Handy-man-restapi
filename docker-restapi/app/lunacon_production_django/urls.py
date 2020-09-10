"""lunaconWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restapi.views import CustomObtainAuthToken, OrderView, ProductOrderView, ProductView, JobSiteView, VendorView, UserView
from restapi.views import HomeView, TermsView, PrivacyView
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import RedirectView
from django.conf.urls import url


router = routers.DefaultRouter()
# router.register(r'equipment status', EquipmentStatusView)

router.register(r'users', UserView)
router.register(r'orders', OrderView)
router.register(r'productOrders', ProductOrderView)
router.register(r'products', ProductView)
router.register(r'jobsite',  JobSiteView)
router.register(r'vendor', VendorView)
# router.register(r'user_info', UserExistsView)
# router.register(r'user', UserExistsView)


urlpatterns = [
    # restapi views
    path('restapi/', include(router.urls)),
    path('admin/', admin.site.urls),

    # token authorization
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    # template views
    path('', HomeView.as_view(), name="home"),
    path('terms/', TermsView.as_view(), name="terms"),
    path('privacy/', PrivacyView.as_view(), name="privacy"),
]
