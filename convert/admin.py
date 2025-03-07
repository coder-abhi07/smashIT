from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.

admin.site.site_header = _("Administration")
admin.site.site_title = _("Administration")
admin.site.index_title = _("Welcome to the Admin Dashboard")