from django import forms
from communityfund.widgets import BSDecimalInput, BSTextInput
from crispy_forms.bootstrap import FormActions, AppendedPrependedText, PrependedAppendedText
from crispy_forms.helper import FormHelper
from django.core.urlresolvers import reverse
from crispy_forms.layout import Submit, Layout, Field, Div, Button, HTML
from communityfund.utils import field_max_len
from communityfund.apps.home.models import Idea, Category
from datetime import datetime, timedelta


class IdeaForm(forms.ModelForm):
    """
    A form that creates a new idea.
    """
    name = forms.CharField(
        label='Name',
        max_length=field_max_len(Idea, 'name'),
        required=True,
        widget=forms.TextInput(),
    )

    category = forms.ModelChoiceField(
        label='Category',
        required=True,
        queryset=Category.objects.all()
    )

    description = forms.CharField(
        label='Description',
        max_length=field_max_len(Idea, 'description'),
        required=True,
        widget=forms.Textarea(attrs={
            'rows': 10,
        }),
    )

    class Meta:
        model = Idea
        fields = ['name', 'category', 'description']

    def save(self, commit=True):
        idea = super(IdeaForm, self).save(commit=False)
        if commit:
            idea.save()
        return idea

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name', placeholder='Idea Name'),
            Field('category'),
            Field('description',
                  placeholder='Description of your idea (max {} characters)'.format(
                      field_max_len(Idea, 'description')))
        )


class IdeaUpdateForm(IdeaForm):
    class Meta(IdeaForm.Meta):
        fields = ['name', 'category', 'description']

        