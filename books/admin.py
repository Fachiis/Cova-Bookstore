from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2


class CustomBookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline
    ]
    list_display = ('title', 'author', 'price',)
    search_fields = ('title',)


admin.site.register(Book, CustomBookAdmin)
