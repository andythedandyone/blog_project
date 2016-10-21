from django.contrib import admin
from .models import blogPost

# Register your models here.


class modeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ('title',)
    search_fields = ('title',)



admin.site.register(blogPost, modeAdmin)



