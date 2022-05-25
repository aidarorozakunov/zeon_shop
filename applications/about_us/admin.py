from django.contrib import admin

from applications.about_us.models import About, AboutImage, Help, NewsImage, News, Advantages


class AboutAdminDisplay(admin.ModelAdmin):
    list_display = ('about', 'description')


class InlineAboutImage(admin.TabularInline):
    model = AboutImage
    extra = 1
    fields = ['image', ]


class HelpAdminDisplay(admin.ModelAdmin):
    list_display = ('question', 'answer')


class NewsAdminDisplay(admin.ModelAdmin):
    list_display = ('image', 'title', 'text')


class InlineNewsImage(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ['image',]


class AdvantagesAdminDisplay(admin.ModelAdmin):
    list_display = ('image', 'title', 'text')


class InlineAdvantagesImage(admin.TabularInline):
    model = Advantages
    extra = 1
    fields = ['image',]


admin.site.register(About, AboutAdminDisplay)
admin.site.register(Help)
admin.site.register(News)
admin.site.register(Advantages)