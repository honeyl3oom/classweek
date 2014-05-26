from django.db import models
from django.contrib.auth.models import User
import datetime

class Company(models.Model):
    name = models.TextField(null=False, unique=True)
    contact = models.TextField(null=True)
    address = models.TextField(null=True)
    zone = models.TextField(null=True)
    nearby_station = models.TextField(null=True)
    introduction = models.TextField(null=True)
    refund_information = models.TextField(null=True)
    facility_information = models.TextField(null=True)
    thumbnail_image_url = models.TextField(null=False, blank=True, default='')
    # toilet, fitting_room, shower_stall, locker, parking_lot, practice_room, instrument_rental
    naver_object_id = models.TextField(null=True)

    def __unicode__(self):
        return 'Company : %s' % self.name

    def __str__(self):
        return unicode(self).encode('utf-8')

# before 20140521
# class Company(models.Model):
#     name = models.TextField( unique=True )
#     phone_number = models.TextField( null=True )
#     location = models.TextField()
#     zone = models.TextField( null=False, blank=True, default='' )
#     naver_object_id = models.TextField(null=True)
#     nearby_station = models.TextField( null=True )
#     facilitiesInformation = models.TextField( null=False, blank=True, default='')
#     thumbnail_image_url = models.TextField(null=False, blank=True, default='')
#     # toilet, fitting_room, shower_stall, locker, parking_lot, practice_room, instrument_rental
#
#     def __str__(self):
#         return 'Company : %s' % self.name
#
#     def __unicode__(self):
#         return 'Company : %s' % self.name

class CompanyReview(models.Model):
    company = models.ForeignKey(Company, related_name='get_company_reviews')
    user = models.ForeignKey(User, related_name='get_company_reviews', null=True, blank=True)
    source = models.TextField(null=False, default='naver')
    contents = models.TextField(null=True)
    score = models.FloatField(default=0.0)
    created = models.DateTimeField(default=datetime.datetime.now)
    is_representing_reivew = models.BooleanField(null=False,default=False)

    class Meta:
        unique_together = (("company", "source", "contents", "created"),)

    def __unicode__(self):
        return '(%r)CompanyReview(%r) : (%r) %s / %s' % (self.id, self.is_representing_reivew, self.score,
                                                         self.company.name, self.contents)

    def __str__(self):
        return unicode(self).encode('utf-8')

class CompanyImage(models.Model):
    company = models.ForeignKey(Company, related_name='get_company_images')
    image_url = models.TextField()

    def __unicode__(self):
        return '(%r)CompanyImage(%r) : %s' % (self.id, self.company.name, self.image_url)

    def __str__(self):
        return unicode(self).encode('utf-8')

class Category(models.Model):
    name = models.TextField( unique=True )

    def __str__(self):
        return 'Category : %s' % self.name

    def __unicode__(self):
        return 'Category : %s' % self.name

class SubCategory(models.Model):
    name = models.TextField(unique=True)
    category = models.ForeignKey(Category, related_name='get_subcategorys')
    name_kor = models.TextField(null=True)
    description = models.TextField(null=True)
    image_url = models.TextField(null=True)
    order_priority_number = models.IntegerField(null=False, default=0)

    def __str__(self):
        return 'SubCategory : %s' % self.name

    def __unicode__(self):
        return 'SubCategory : %s' % self.name

class SubCategoryRecommend(models.Model):
    image_url = models.TextField(null=True)

class Classes(models.Model):
    title = models.TextField(null=False)
    sub_category = models.ForeignKey(SubCategory, related_name='get_classes')
    company = models.ForeignKey(Company)
    description = models.TextField(null=True)
    personal_or_group = models.TextField(null=False,default='personal') # personal or group
    is_allowed_one_day = models.BooleanField(null=False,default=False)
    price_of_one_day = models.IntegerField(null=False,default=0)
    count_of_week = models.IntegerField(null=False,default=0)
    count_of_month = models.IntegerField(null=False,default=0)
    price_of_month = models.IntegerField(null=False,default=0)
    preparation = models.TextField(null=True)
    maximum_number_of_enrollment = models.IntegerField(null=False,default=0)
    curriculum_in_first_week = models.TextField(null=True)
    curriculum_in_second_week = models.TextField(null=True)
    curriculum_in_third_week = models.TextField(null=True)
    curriculum_in_fourth_week = models.TextField(null=True)
    curriculum_in_fifth_week = models.TextField(null=True)

    class Meta:
        unique_together = (("title", "sub_category", "company", "personal_or_group"),)

    def __unicode__(self):
        return '(%r)Classes(%r) : %s' % (self.id, self.sub_category.name, self.title)

    def __str__(self):
        return unicode(self).encode('utf-8')


# before 20140521
# class Classes(models.Model):
#     title = models.TextField( null=True )
#     thumbnail_image_url = models.TextField( null=True )
#     subCategory = models.ForeignKey( SubCategory, related_name='get_classes' )
#     company = models.ForeignKey( Company )
#     description = models.TextField( null=True )
#     preparation = models.TextField( null=True )
#     personalOrGroup = models.TextField( null=True )
#     refundInformation = models.TextField( null=True )
#     # countOfDay = models.IntegerField( null=True )
#     priceOfDay = models.IntegerField( null=True )
#     countOfMonth = models.IntegerField( null=True )
#     priceOfMonth = models.IntegerField( null=True )
#     image_url = models.TextField( null=True )
#
#     class Meta:
#         unique_together = (("title", "thumbnail_image_url", "subCategory", "company", "description", "preparation", "personalOrGroup", "refundInformation", "priceOfDay", "countOfMonth", "priceOfMonth", "image_url"),)
#
#     def __str__(self):
#         return '(%d)Classes : %s / %s' % (self.id, self.title, self.description )
#
#     def __unicode__(self):
#         return '(%d)Classes : %s / %s' % (self.id, self.title, self.description )

class ClassesImage(models.Model):
    classes = models.ForeignKey(Classes, related_name='get_images')
    image_url = models.TextField()

class ClassesInquire(models.Model):
    classes = models.ForeignKey(Classes)
    user = models.ForeignKey(User)
    content = models.TextField(null=False, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)

class Schedule(models.Model):
    classes = models.ForeignKey(Classes , related_name='get_schedules')
    weekday_list = models.CharField(max_length=27) # Mon=1, Tue=2, Wed, Thu, Fri, Sat, Sun
    start_time_list = models.TextField(null=True)
    duration = models.TimeField(default='00:00:00')

    def __unicode__(self):
        return '(%r)Schedule class_id(%r) weekday_list(%r) start_time_list(%r) duration(%r) ' \
               % (self.id, self.classes_id, self.weekday_list, self.start_time_list, self.duration)

    def __str__(self):
        return unicode(self).encode('utf-8')

# before 20140521
# class Schedule(models.Model):
#     classes = models.ForeignKey( Classes , related_name='get_schedules')
#     # Mon=1, Tue=2, Wed, Thu, Fri, Sat, Sun
#     dayOfWeek = models.CharField( max_length=27 )
#     startTime = models.TextField( null=True )
#     duration = models.TimeField( default='00:00:00')
#
#     def __str__(self):
#         return 'class_id=(%d), (%d)Schedule : %s %r' % (self.classes_id, self.id, self.dayOfWeek, self.startTime )
#
#     def __unicode__(self):
#         return 'class_id=(%d), (%d)Schedule : %s %r' % (self.classes_id, self.id, self.dayOfWeek, self.startTime )

class ClassesRecommend(models.Model):
    classes = models.ForeignKey(Classes, related_name='get_recommends')
    schedule = models.ForeignKey(Schedule, related_name='get_recommends')
    order_priority_number = models.IntegerField(null=False, default=0)

    def __str__(self):
        return 'ClassesRecommend : %d %r %r' % (self.id, self.classes, self.schedule)

class Promotion(models.Model):
    start_date = models.DateField(null=False)
    daily_start_time = models.TimeField(null=False)
    end_date = models.DateField(null=False)
    daily_end_time = models.TimeField(null=False)
    discount_percentage = models.IntegerField(null=False, default=0)
    total_maximum_count = models.IntegerField(null=False, default=0)
    daily_maximum_count = models.IntegerField(null=False, default=0)

class PromotionDetail(models.Model):
    promotion = models.ForeignKey(Promotion, related_name='get_promotion_details')
    purchase = models.ForeignKey('foradmin.Purchase')
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)