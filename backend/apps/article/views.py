from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import serializers, status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article, PostImage
from .serializer import ArticleSerializer, PosterSerializer
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.prefetch_related('images').all()
    permission_classes = [IsAuthenticated]
    serializer_class = PosterSerializer
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'new_post':
            return PosterSerializer
        return super().get_serializer_class()
    
    @action(detail=False, methods=['post'])
    def new_post(self, request):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    
