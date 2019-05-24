from django.contrib import admin
from app01 import models

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'pub_date')
    list_editable = ('name', 'price', 'pub_date')
    list_filter = ('pub_date', 'publish')
    list_per_page = 5
    filter_horizontal = ('authors',)
    search_fields = ('id', 'name', 'price', 'publish__name')
    ordering = ("id",)


class BookAuthor(admin.ModelAdmin):
    list_display = ("name", "age")


admin.site.register(models.Author, BookAuthor)
admin.site.register(models.Publish)
admin.site.register(models.Book, BookAdmin)



