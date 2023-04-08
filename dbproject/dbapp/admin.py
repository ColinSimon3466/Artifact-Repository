from django.contrib import admin

# Register your models here.


from .models import Artifact



class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    search_fields = ['Name','Level',]
    list_filter = ('Level',)

admin.site.register(Artifact, ArtifactAdmin)