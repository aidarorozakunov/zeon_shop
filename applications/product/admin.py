from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.product.models import Product, ProductImage


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'color']
    max_num = 8
    # def get_max_num(self, request, obj=None, **kwargs):
    #     max_num = 8
    #     if obj and obj.parent:
    #         return max_num - 5
    #     return max_num


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]
    list_display = ('title', 'hit', 'quantity', 'image', )
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



