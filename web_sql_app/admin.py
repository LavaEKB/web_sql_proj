from django.contrib import admin
from .models import Cards, Sale, Talon

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cards, PostAdmin)
admin.site.register(Sale, PostAdmin)
admin.site.register(Talon, PostAdmin)