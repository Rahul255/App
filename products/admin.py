from django.contrib import admin

# Register your models here.
from .models import Pooja, Comment, Print


@admin.register(Pooja)
class PoojaAdmin(admin.ModelAdmin):
    list_display = ('pooja', 'price', 'god', 'date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('pooja', 'comment')


@admin.register(Print)
class PrintAdmin(admin.ModelAdmin):
    list_display = ()
