from django.contrib import admin
from .models import Bb, Rubric, Aa, Training, news, ModelPrac9, \
    AdvUser, Spare, Machine, Measure, Comment, Rubric_new, Note
from mptt.admin import MPTTModelAdmin


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Note)

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(Aa)
admin.site.register(Training)
admin.site.register(news)
admin.site.register(ModelPrac9)
admin.site.register(AdvUser)
admin.site.register(Spare)
admin.site.register(Machine)
admin.site.register(Measure)
admin.site.register(Comment)

admin.site.register(Rubric_new)


class Rubric_newAdmin(MPTTModelAdmin):
    list_display = ("name", "parent", "id")
    mptt_level_indent = 20
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "parent")

