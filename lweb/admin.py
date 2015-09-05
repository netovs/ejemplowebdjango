from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea



from lweb.models import Categoria, Temas

class CategoriaAdmin(admin.ModelAdmin):
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':60})},
    }

    
    fieldsets = [
        (None,               {'fields': ['nombre']}),
        ('Descripcion',        {'fields': ['descripcion']}),
        ('Fecha', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Recetas', {'fields': ['receta'], 'classes': ['collapse']}),
    ]
    
    list_display = ('nombre', 'pub_date')    
    list_filter = ['pub_date']
admin.site.register(Categoria, CategoriaAdmin)


class TemasAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':80})},
        
    }

    raw_id_fields = ('catid',)
   
    
    fieldsets = [
        ('Selecciona el tema',      {'fields': ['catid']}),
        (None,                      {'fields': ['titulo_tema']}),
        ('Contenido',               {'fields': ['contenido_tema']}),
        ('Imagen',                  {'fields': ['nombre_imagen']}),
        ('Menu',                    {'fields': ['menu']}),
        ('Publicado',               {'fields': ['activo']}),
        
        
    ]
    
    list_filter = ['activo']
    list_display = ('titulo_tema', 'activo')
    

    

admin.site.register(Temas, TemasAdmin)



