from django.contrib import admin
from team.models import Member

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    fields = ['last_name', 'first_name']
    ordering = ['last_name', 'first_name']


admin.site.register(Member, MemberAdmin)
