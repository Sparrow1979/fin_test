# admin.py
from django.contrib import admin
from django.template.response import TemplateResponse
from .models import Company  # Import your models here

#def custom_admin_index(request, extra_context=None):
#    context = {
#        **admin.site.each_context(request),
#        'user': request.user,  # Ensuring `user` is the authenticated User object
#    }
#    return TemplateResponse(request, "admin/index.html", context)

#admin.site.index_template = 'admin/index.html'
#admin.site.index = custom_admin_index

# Register your models here
@admin.register(Company)
class YourModelAdmin(admin.ModelAdmin):
    pass  # Customize the admin class if needed



