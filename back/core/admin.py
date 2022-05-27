from django.contrib import admin
from django.forms import ModelForm, TextInput, ModelMultipleChoiceField
from easy_select2 import Select2Multiple

from .models import BusinessDomains, Tables, Tags, TagsType


class BusinessDomainsForm(ModelForm):
    table = Tables.objects.all()
    tables = ModelMultipleChoiceField(
        queryset=table,
        widget=Select2Multiple(select2attrs={'width': '300px'}),
        blank=True,
        required=False,
    )

    class Meta:
        model = BusinessDomains
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
            'tables': Select2Multiple(
                select2attrs={'width': '300px'}
            ),
            'tags': Select2Multiple(
                select2attrs={'width': '300px'}
            ),
        }


@admin.register(BusinessDomains)
class BusinessDomainsAdmin(admin.ModelAdmin):
    form = BusinessDomainsForm
    list_display = ('id', 'name', 'color', 'parent')
    list_filter = ('parent',)
    list_editable = ('name', 'color')
    search_fields = ('^name',)
    save_on_top = True


class TablesForm(ModelForm):
    tag = Tags.objects.all()
    tags = ModelMultipleChoiceField(
        queryset=tag,
        widget=Select2Multiple(select2attrs={'width': '300px'}),
        blank=True,
        required=False,
    )

    class Meta:
        model = Tables
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
            'tags': Select2Multiple(
                select2attrs={'width': '300px'}
            ),
        }


@admin.register(Tables)
class TablesAdmin(admin.ModelAdmin):
    form = TablesForm
    list_display = ('id', 'name', 'color',)
    list_editable = ('name', 'color')
    search_fields = ('^name',)
    save_on_top = True


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    form = TagsForm
    list_display = ('id', 'name', 'color',)
    list_editable = ('name', 'color')
    search_fields = ('^name',)
    save_on_top = True


class TagsTypeForm(ModelForm):
    class Meta:
        model = TagsType
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }


@admin.register(TagsType)
class TagsTypeAdmin(admin.ModelAdmin):
    form = TagsTypeForm
    list_display = ('id', 'name', 'color',)
    list_editable = ('name', 'color')
    search_fields = ('^name',)
    save_on_top = True
