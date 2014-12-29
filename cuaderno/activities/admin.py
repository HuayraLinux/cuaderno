
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

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
    list_display = ['name', 'organizer', 'location', 'kind', 'owner']
    list_filter = ['kind', 'organizer', 'from_date']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user

        super(ActivityAdmin, self).save_model(request, obj, form, change)

    def queryset(self, request):
        qs = super(ActivityAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if not self.queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:activities_activity_changelist'))

        return super(ActivityAdmin, self).change_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        if not self.queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:activities_activity_changelist'))

        return super(ActivityAdmin, self).delete_view(request, object_id, extra_context)

    def history_view(self, request, object_id, extra_context=None):
        if not self.queryset(request).filter(id=object_id).exists():
            return HttpResponseRedirect(reverse('admin:activities_activity_changelist'))

        return super(ActivityAdmin, self).history_view(request, object_id, extra_context)



admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityURL, ActivityURLAdmin)
admin.site.register(ActivityKind, ActivityKindAdmin)
admin.site.register(ActivityAttachment, ActivityAttachmentAdmin)
