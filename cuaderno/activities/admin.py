from django.contrib import admin
from activities.models import Activity, ActivityURL, ActivityKind

# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    pass


class ActivityURLAdmin(admin.ModelAdmin):
    pass


class ActivityKindAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityURL, ActivityURLAdmin)
admin.site.register(ActivityKind, ActivityKindAdmin)
