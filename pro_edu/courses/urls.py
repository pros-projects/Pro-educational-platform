from django.urls import include,path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('courses',views.CoursesViewSet)
router.register('sections',views.SectionViewSet)
router.register('videos',views.VideoViewSet)

urlpatterns = router.urls

