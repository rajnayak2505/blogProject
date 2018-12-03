from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','body','publish','created','updated','status')

    # -------------------prepopulated_fields  is for automatitically fill the slug by the reffrence of title------------------
    prepopulated_fields={'slug':('title',)}

    # ------------------------------we can filter the blog bye list_filter-------------------------------------------------------
    list_filter=('status','author','created','publish')

    # ---------------------------we can  search blog via search_fields to using keywords title or body or many more--------------
    search_fields=('title','body')

    # ---------------------we can search by id in  databases without using dropdwon-----------------------------
    raw_id_fields=('author',)

    # ------------------------date_hierarchy is it will show navbar of date of post------------------------------
    date_hierarchy='publish'

    # --------------------------ordering is showing  numbering in list_display-------------
    ordering=['status','publish']


# Register your models here.
admin.site.register(Post, PostAdmin)






























# -------------------------------------------
