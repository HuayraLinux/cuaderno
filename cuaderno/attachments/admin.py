from django.contrib import admin
from attachments.models import Attachment

# Register your models here.

class AttachmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attachment, AttachmentAdmin)
