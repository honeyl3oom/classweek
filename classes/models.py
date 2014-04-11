from django.db import models

class Company(models.Model):
    name = models.TextField( unique=True )
    phonenumber = models.TextField()
    location = models.TextField()
    nearby_station = models.TextField()
    facilitiesInfomation = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 'Company : %s' % self.name

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
    title = models.TextField()
    subCategory = models.ForeignKey( SubCategory )
    company = models.ForeignKey( Company )
    short_description = models.TextField()
    description = models.TextField()
    preparation = models.TextField()
    zone = models.TextField()
    personalOfGroup = models.TextField()
    refundInfomation = models.TextField()
    countOfDay = models.IntegerField()
    priceOfDay = models.IntegerField()
    countOfMonth = models.IntegerField()
    priceOfMonth = models.IntegerField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return 'Classes : %s' % self.title

class Schedule(models.Model):
    classes = models.ForeignKey( Classes )
    # Sun, Mon, Tue, Wed, Thu, Fri, Sat
    dayOfWeek = models.CharField( max_length=3 )
    startTime = models.TimeField( auto_now=True )

    def __str__(self):
        return self.dayOfWeek

    def __unicode__(self):
        return 'Schedule : %s %d' % ( self.dayOfWeek, self.startTime )
