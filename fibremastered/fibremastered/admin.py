from django.contrib import admin

from fibremastered.models import Site, Template
from django.contrib import admin


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass

