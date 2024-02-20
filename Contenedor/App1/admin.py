from django.contrib import admin
from .models import AutorDb, FraseDb, Profesion
# Register your models here.

admin.site.site_header = "CS"
admin.site.index_title = "22"
admin.site.site_title = "33"


@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    fields = ["nombre"]

class FraseInLine(admin.TabularInline):
    model = FraseDb
    Extra = 1

class AutorAdmin(admin.ModelAdmin):
    fileds = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad"]
    lists_display = ["nombre", "fecha_nacimiento"]

    inlines = [FraseInLine]

    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O", "o")
                obj.save()

        self.message_user(request, "Exitosamente")
    actualizar_o.short_description = "Actualizar letras O"

    actions = ["actualizar_o"]

admin.site.register(AutorDb, AutorAdmin)

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fileds = ["cita", "autor_fk"]
    lists_display = ["cita"]