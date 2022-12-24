from django.urls import path,include
from .views import FooterView,HeaderView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('footer', FooterView)
router.register('header', HeaderView)

urlpatterns = router.urls