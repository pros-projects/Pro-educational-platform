from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter,DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



router = DefaultRouter()
router.register('register',views.RegistrationApi)

urlpatterns =router.urls+ [
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
]