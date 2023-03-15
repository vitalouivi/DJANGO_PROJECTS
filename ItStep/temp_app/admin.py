from django.contrib import admin
from .models import Temp, Message, PrivateMessage, Note, PrivateNote, Message_from_abstract, Note_1


class TempAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'slug')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Temp, TempAdmin)

admin.site.register(Message)
admin.site.register(Note_1)
#admin.site.register(Note)
admin.site.register(PrivateNote)
admin.site.register(Message_from_abstract)
admin.site.register(PrivateMessage)
