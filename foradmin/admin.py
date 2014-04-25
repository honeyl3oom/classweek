from django.contrib import admin
from foradmin.models import ApiLog, UserSession

# class CompanyAdmin( admin.ModelAdmin ):
#     pass
#
# admin.site.register(Company, CompanyAdmin)

admin.site.register(ApiLog)
admin.site.register(UserSession)