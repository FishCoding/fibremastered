from django.db import models
from django.contrib.contenttypes.models import ContentType

from sitetree.models import TreeItemBase

from django_editorjs import EditorJsField

## mediastorage formats
FORMATS = {
    'fullscreen': (1920, 1280),
}


class Template(models.Model):
    name = models.CharField(max_length=200)
    template_path = models.CharField(max_length=250, help_text="Format: app/template_name.html")

    def __str__(self):
        return self.name


class Site(TreeItemBase):
    display_title = models.CharField(default='', max_length=250, blank=True)
    body = EditorJsField(null=True, blank=True)
    transfer_model = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)


    class Meta:
        unique_together = []

    def __str__(self):
        return self.title
