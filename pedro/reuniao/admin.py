from django.contrib import admin
from .models import Reuniao
from import_export.admin import ImportExportModelAdmin


@admin.register(Reuniao)
class alunosadmin (ImportExportModelAdmin):
    list_display = ('name', 'serie', 'turma', 'ausente')
    list_filter = ("turma", "serie",)
    search_fields = ("name", "serie", "turma",)




