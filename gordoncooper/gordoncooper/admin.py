from django.contrib import admin
from gordoncooper.models import Image, Post


class ImageAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'type')
    list_filter = ('type',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('images',)
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
