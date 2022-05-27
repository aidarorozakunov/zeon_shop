from django.contrib import admin

from applications.about_us.models import Help, NewsImage, News, Advantages, Offer, HelpImage, About, AboutImage


class HelpAdminDisplay(admin.ModelAdmin):
    list_display = ('question', 'answer')


class InlineHelpImage(admin.ModelAdmin):
    model = HelpImage
    fields = ['image',]


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


class OfferAdminDisplay(admin.ModelAdmin):
    list_display = ('title', 'offer')


class AboutAdminDisplay(admin.ModelAdmin):
    list_display = ('about', 'description')


class InlineAboutImage(admin.TabularInline):
    model = AboutImage
    extra = 1
    fields = ['image', ]


admin.site.register(Help)
admin.site.register(News)
admin.site.register(Advantages)
admin.site.register(Offer)
admin.site.register(About)