from django.contrib import admin

from business_api import models
from import_export.admin import ExportActionMixin
from rest_framework.authtoken.models import Token


# Register your models here.

class CashBackAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['reference', 'transaction_type']


admin.site.register(models.CustomUser)
admin.site.register(models.Transaction, CashBackAdmin)
admin.site.register(models.Blacklist)
admin.site.register(models.MTNToggle)