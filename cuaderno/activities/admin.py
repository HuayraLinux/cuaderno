from django.contrib import admin
from activities.models import Activity, ActivityURL, ActivityKind, ActivityAttachment

# Register your models here.

class ActivityURLAdmin(admin.ModelAdmin):
    pass


class ActivityKindAdmin(admin.ModelAdmin):
    pass


class ActivityAttachmentAdmin(admin.ModelAdmin):
    pass


class ActivityURLInline(admin.TabularInline):
    model = ActivityURL


class ActivityAttachmentInline(admin.StackedInline):
    model = ActivityAttachment


class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityURLInline, ActivityAttachmentInline]
    list_display = ['name', 'organizer', 'location', 'kind']
    list_filter = ['kind', 'organizer', 'from_date']

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityURL, ActivityURLAdmin)
admin.site.register(ActivityKind, ActivityKindAdmin)
admin.site.register(ActivityAttachment, ActivityAttachmentAdmin)
