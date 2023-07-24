from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Article

class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title', 'user', 'content','last_modified')
    list_filter = ("title", "user")
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Article, ArticleAdmin)