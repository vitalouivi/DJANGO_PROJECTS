from django.core.exceptions import ValidationError
from django.forms import modelform_factory, DecimalField, ModelForm, modelformset_factory
from django.forms.widgets import Select, __all__
from django import forms
from django.core import validators
from django.http import HttpResponse

from .models import Temp

Temp1Form = modelform_factory(Temp,
                              fields=('title',  'slug',),
                              exclude=('published', 'price', 'content',),
                              labels={'title': 'Название Темплэйта', 'price': 'Ценник', 'slug':'unique url'},
                              error_messages={ValidationError: {
                                            'slug': 'slug is not unique',
                                             'title': 'title is not defined',
                                             'price': 'price is not valid',
                                             'content': 'content is not valid',
                                             'published': 'time wrong'}},
                              help_texts={'slug': 'Должно быть уникальным', 'content':'пожалуйста заполни' },
                              field_classes={'price': DecimalField, })




class Temp2Form(ModelForm):
    class Meta:
        model = Temp
        fields = ('title', 'price', 'content', 'slug')
        labels = {'title': 'Название Темплэйта', 'price': 'Ценник', 'slug': 'unique url'}
        error_messages = {ValidationError: {
            'slug': 'slug is not unique',
            'title': 'title is not defined',
            'price': 'price is not valid',
            'content': 'content is not valid',
            'published': 'time wrong'}}
        help_texts = {'slug': 'Должно быть уникальным', 'content': 'пожалуйста заполни'}
        field_classes = {'price': DecimalField, }


def myvalidator(val):
    if val != 'AAAA':
        raise ValidationError('title is not correct')


class Temp3Form(forms.ModelForm):
    title = forms.CharField(
        label='Название темплейта',
        max_length=50,
        #validators=[myvalidator],
        #validators=[validators.RegexValidator(regex='^.{4,}$')],
        error_messages={'invalid': 'Слишком короткое название'})
    #price = forms.DecimalField(label='ценник', decimal_places=3)
    #content = forms.CharField(label='Содержимое темплейта', widget=forms.Textarea)
    slug = forms.SlugField(label='адрес', help_text='Должно быть уникальным')
    #published = forms.DateTimeField(label='', help_text='', label_suffix='', initial='', required=True, widget=Select, validators='', error_messages={},  )

    class Meta:
        model = Temp
        fields = ('title', 'slug')

    def clean(self):
        super().clean()
        errors = {}
        if self.cleaned_data['title'] == 'BB' or self.cleaned_data['title'] == 'AA':
            errors['title'] = ValidationError('title is not allowed')
        #if self.cleaned_data['price'] <= 0:
        #    errors['title'] = ValidationError('Fill in the price correctly')
        if errors:
            raise ValidationError(errors)


class Temp4Form(forms.ModelForm):
    title = forms.CharField(label='Название темплейта', max_length=50, initial='some price')
    price = forms.DecimalField(label='ценник', decimal_places=2, label_suffix='|------->', initial=0, required=False, disabled=True )

    class Meta:
        model = Temp
        fields = ('title', 'price', 'content', 'slug')


formset = modelformset_factory(Temp,
                               form=Temp1Form,
                               #fields=('title', 'slug',),
                               #exclude=('content', 'published', 'price', ),
                               #error_messages=
                               #help_texts=
                               #labels=
                               #changed_objects, new_objects, deleted_objects
                               extra=1, can_order=True, can_delete=True,
                               min_num=1, validate_min=True,
                               max_num=100, validate_max=True,
                               )


