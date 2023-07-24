from rest_framework import serializers
from .models import Article, PostImage

from django import forms
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = '__all__'
        

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'


class PostImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = PostImage
        fields = '__all__'


class PosterSerializer(serializers.ModelSerializer):
    images= PostImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=100, allow_empty_file=False, use_url=False),
        write_only = True
    )
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'last_modified', 'images', 'uploaded_images')
        
    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_article = Article.objects.create(**validated_data, user=self.context['request'].user)
        print(new_article)
        for uploaded_item in uploaded_data:
            PostImage.objects.create(article=new_article, image=uploaded_item)
        return new_article
    
    def update(self, instance, validated_data):
        updated_data = validated_data.pop('uploaded_images')
        super().update(instance, validated_data)
        PostImage.objects.filter(article=instance).delete()
        for update_item in updated_data:
            PostImage.objects.create(article=instance, image=update_item)
        return instance