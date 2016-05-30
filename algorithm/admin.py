from django.contrib import admin
from .models import RSA


class RSAAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['a1b1', 'a2b2']
    search_fields = ['title']
    save_on_top = True

admin.site.register(RSA, RSAAdmin)
