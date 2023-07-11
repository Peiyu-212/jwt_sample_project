from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import ArticleViewSet

router = routers.DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path('', include((router.urls))),
]
