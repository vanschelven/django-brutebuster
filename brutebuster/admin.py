# brutebuster by Cyber Security Consulting (www.csc.bg)

"""Admin settings for the brutebuster module"""

from django.contrib import admin
from brutebuster.models import FailedAttempt


class AdminFailedAttempt (admin.ModelAdmin):
    list_display = ('username', 'IP', 'failures', 'timestamp', 'blocked')
    search_fields = ('username', 'IP', )


admin.site.register(FailedAttempt, AdminFailedAttempt)
