from django.contrib import admin
from .models import *

class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
            obj.save()
    
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget},
    }

admin.site.register(Contact)
admin.site.register(JobListing,JobListingAdmin)
admin.site.register(ApplyJob)

