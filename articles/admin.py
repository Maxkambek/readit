from django.contrib import admin
from .models import Tag,Category,Article,Comment


class TagAdmin(admin.ModelAdmin):
    list_display = ('id','tag')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','created_at')
    list_filter = ('updated_at','created_at')
    search_fields = ('title','updated_at')
    readonly_fields = ('updated_at','created_at')
    prepopulated_fields = ({'slug':('title',)})
    filter_horizontal = ('tag',)


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','id')
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','name','email','created_at')
    list_filter = ('created_at',)
    search_fields = ('name','email')
    readonly_fields = ('article',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)

