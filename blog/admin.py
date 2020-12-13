from django.contrib import admin
from django.utils.encoding import force_text
from .models import Module, Instructor, Content_Type, ModuleInstance 
#admin.site.register(Post)
"""
admin.site.register(Module)
admin.site.register(Instructor)
admin.site.register(Content_Type)
admin.site.register(ModuleInstance)
"""
admin.site.register(Content_Type)

class ModuleInline(admin.TabularInline):
    """Defines format of inline module insertion (used in InstructorAdmin)"""
    model = Module


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    """Administration object for Instructor models."""
    list_display = ('last_name',
                    'first_name', 'email')
    fields = ['first_name', 'last_name', 'email']
    inlines = [ModuleInline]


class ModuleInstanceInline(admin.TabularInline):
    """Defines format of inline Module instance insertion (used in ModuleAdmin)"""
    list_filter = ('status', 'start_date')
    model = ModuleInstance


class ModuleAdmin(admin.ModelAdmin):
    """Administration object for Module models."""
    
    list_display = ('title', 'instructor','display_content_type')
    inlines = [ModuleInstanceInline]


admin.site.register(Module, ModuleAdmin)


@admin.register(ModuleInstance)
class ModuleInstanceAdmin(admin.ModelAdmin):
    """Administration object for ModuleInstance models."""
    list_display = ('module', 'status', 'start_date', 'id')
    list_filter = ('status', 'start_date')

    fieldsets = (
        (None, {
            'fields': ('module', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'start_date')
        }),
    )
