from django.contrib import admin
from classes.models import Company, CompanyImage, Category, SubCategory, SubCategoryRecommend,\
Classes, ClassesImage, ClassesInquire, Schedule, ClassesRecommend

# class CompanyAdmin( admin.ModelAdmin ):
#     pass
#
# admin.site.register(Company, CompanyAdmin)

admin.site.register(Company)
admin.site.register(CompanyImage)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubCategoryRecommend)
admin.site.register(Classes)
admin.site.register(ClassesImage)
admin.site.register(ClassesInquire)
admin.site.register(Schedule)
admin.site.register(ClassesRecommend)