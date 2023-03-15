from django.contrib.contenttypes.forms import generic_inlineformset_factory
from django.forms import ModelForm
from .models import Bb, Aa, Training, Comment, Note
from django import forms


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'slug')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'comment')


class AaForm(ModelForm):
    class Meta:
        model = Aa
        fields = ('title', 'content', 'price')


class TestForm(ModelForm):
    class Meta:
        model = Training
        fields = ('chfield1', 'chfield2', 'chfield3', 'tfield1', 'tfield2', 'ffield', 'ifield', 'dfield')


NoteForm = generic_inlineformset_factory(Note,
                                         #content_type_field='content_type',
                                         #object_id_field='object_id',
                                         for_concrete_model=True, #Если любая из моделей - прокси модель, то надо указать False
                                         ) #Аналогично с FormSetFactory