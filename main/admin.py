from django.contrib import admin
from main.models import Domaine, Branche, Qcm

class QcmAdmin(admin.ModelAdmin):
    list_display = ('question', 'reponse', "branche")
    list_filter = ['branche', 'branche__domaine']
    search_fields = ['question']
    ordering = ('branche__domaine',)

class BrancheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'domaine')
    list_filter = ['domaine']

admin.site.register(Domaine)
admin.site.register(Branche, BrancheAdmin)
admin.site.register(Qcm, QcmAdmin)

