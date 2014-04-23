from django.contrib import admin
from classes.models import Company, Category, SubCategory, Classes, Schedule, SubCategoryRecommend, ClassesRecommend

class CompanyAdmin( admin.ModelAdmin ):
    pass

class CategoryAdmin( admin.ModelAdmin ):
    pass

class SubCategoryAdmin( admin.ModelAdmin ):
    pass

class ClassesAdmin( admin.ModelAdmin ):
    pass

class ScheduleAdmin( admin.ModelAdmin ):
    pass

admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register( SubCategoryRecommend )
admin.site.register( ClassesRecommend )