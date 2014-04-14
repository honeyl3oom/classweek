from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.TextField( unique=True )
    phonenumber = models.TextField()
    location = models.TextField()
    nearby_station = models.TextField( null=True )
    facilitiesInfomation = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 'Company : %s' % self.name

class CompanyImage(models.Model):
    company = models.ForeignKey( Company )
    image_url = models.URLField()

class Category(models.Model):
    name = models.TextField( unique=True )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 'Category : %s' % self.name

class SubCategory(models.Model):
    name = models.TextField( unique=True )
    category = models.ForeignKey( Category )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 'SubCategory : %s' % self.name

class Classes(models.Model):
    title = models.TextField( null=False, blank=True, default='' )
    subCategory = models.ForeignKey( SubCategory )
    company = models.ForeignKey( Company )
    short_description = models.TextField( null=False, blank=True, default='' )
    description = models.TextField( null=False, blank=True, default='' )
    preparation = models.TextField( null=False, blank=True, default='' )
    zone = models.TextField( null=False, blank=True, default='' )
    personalOrGroup = models.TextField( null=False, blank=True, default='' )
    refundInfomation = models.TextField( null=False, blank=True, default='' )
    # countOfDay = models.IntegerField( null=False, blank=True, default=0 )
    priceOfDay = models.IntegerField( null=False, blank=True, default=0 )
    countOfMonth = models.IntegerField( null=False, blank=True, default=0 )
    priceOfMonth = models.IntegerField( null=False, blank=True, default=0 )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return 'Classes : %s / %s' % (self.title, self.short_description )

class ClassesImage(models.Model):
    classes = models.ForeignKey( Classes )
    image_url = models.URLField()

class ClassesInquire(models.Model):
    classes = models.ForeignKey( Classes )
    user = models.ForeignKey( User )
    content = models.TextField( null=False, blank=True, default='' )

class Schedule(models.Model):
    classes = models.ForeignKey( Classes )
    # Sun, Mon, Tue, Wed, Thu, Fri, Sat
    dayOfWeek = models.CharField( max_length=21 )
    startTime = models.TimeField()
    duration = models.TimeField( default='00:00:00')

    def __str__(self):
        return self.dayOfWeek

    def __unicode__(self):
        return 'Schedule : %s %r' % ( self.dayOfWeek, self.startTime )
