from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.collection.models import Collections, CollectionsImage


class InlineColletionsImage(admin.TabularInline):
    model = CollectionsImage
    extra = 1
    fields = ['image', ]


class CollectionsAdminDisplay(admin.ModelAdmin):
    inlines = [InlineColletionsImage, ]
    list_display = ('title', 'image')
    # list_editable = ('in_stock', 'quantity')
    search_fields = ('title', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(Collections, CollectionsAdminDisplay)

