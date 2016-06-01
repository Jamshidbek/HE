from django.contrib import admin
from .models import RSA, Sezar, Paillier


class RSAAdmin(admin.ModelAdmin):
    fields = [
        'author',
        'title',
        'e',
        'd',
        'public_key',
        'private_key',
        'a1',
        'b1',
        'a2',
        'b2',
        'a1b1',
        'a2b2',
        'ba',
    ]
    list_display = ['title']
    list_filter = ['a1b1', 'a2b2']
    search_fields = ['title']
    save_on_top = True


class SezarAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['a1b1']
    search_fields = ['title']
    save_on_top = True


class PaillierAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['a1b1']
    search_fields = ['title']
    save_on_top = True


admin.site.register(RSA, RSAAdmin)
admin.site.register(Sezar, SezarAdmin)
admin.site.register(Paillier, PaillierAdmin)
