from django.views.generic.base import TemplateView
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Article
from .serializer import PosterSerializer
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.prefetch_related('images').all()
    permission_classes = [IsAuthenticated]
    serializer_class = PosterSerializer
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def new_post(self, request):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    
class ArticleView(TemplateView):
    template_name = "article.html"