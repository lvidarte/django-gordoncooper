from django.contrib import admin
from gordoncooper.models import Image, Post


class ImageAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
