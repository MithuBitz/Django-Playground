from django.contrib import admin

from .models import NamesList, NameReview, DevCommunity, DevCertificate

# Register your models here.
class NameReviewInline(admin.TabularInline):
    model = NameReview
    extra = 2

class NameListAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'add_time')
    inlines = [NameReviewInline]

class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    filter_horizontal = ('name_lists',)

class DevCerficateAdmin(admin.ModelAdmin):
    list_display = ('dev_name', 'certificate_number')

admin.site.register(NamesList, NameListAdmin)
admin.site.register(DevCommunity, CommunityAdmin)
admin.site.register(DevCertificate, DevCerficateAdmin)

