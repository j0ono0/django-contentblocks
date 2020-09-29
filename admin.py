from django import forms
from django.contrib import admin
from .models import ContentBlock


class ContentBlockAdminForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = '__all__'


class ContentBlockAdmin(admin.ModelAdmin):
    form = ContentBlockAdminForm


admin.site.register(ContentBlock, ContentBlockAdmin)