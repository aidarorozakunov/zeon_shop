from ckeditor_uploader import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.product.models import Product, ProductImage
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]
    list_display = ('title', 'hit', 'quantity', 'image', 'color')
    list_editable = ('hit', 'quantity')
    search_fields = ('title', )
    list_filter = ('collections', )

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(Product, ProductAdminDisplay)



