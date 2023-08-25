from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    #readonly_fields=("slug",)
    prepopulated_fields={"course_slug":("course_name",)}
    # list_filter=("author","rating")
admin.site.register(Post,PostAdmin)
# admin.site.register(Post)
