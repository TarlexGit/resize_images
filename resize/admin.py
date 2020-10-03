from django.contrib import admin
from .models import Image_model
# Register your models here.

@admin.register(Image_model) 
class ImagesAdmin(admin.ModelAdmin): 
    list_display = ["image_file", "pk"]
    list_display_links = ("image_file",)
    # prepopulated_fields = {"slug": ("title",)}

