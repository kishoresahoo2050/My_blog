from django.contrib import admin
from .models import  Contact,Post
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']



@admin.register(Post)
class PostAdmiin(admin.ModelAdmin):
    list_display = ['title','auth','desc']