# -*- coding: utf8-*-

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from registration.signals import user_registered


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CompanyMasterProfile(TimeStampedModel):
    user = models.OneToOneField(User, unique=True, related_name='master_profile')
    company_name = models.CharField(max_length=100, blank=True)
    local_number = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    nearby_station = models.CharField(max_length=30, blank=True)
    refund_information = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('forcompany:index', args=[])

    def __unicode__(self):
        return '(%r)CompanyMasterProfile : username[%r]' \
               % (self.id, self.user.username)

    def __str__(self):
        return unicode(self).encode('utf-8')

class CompanyClasses(TimeStampedModel):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    sub_category = models.ForeignKey('classes.SubCategory')
    description = models.TextField(null=True)
    PERSON_OR_GROUP_CHOICES = (
        ('personal', '개인레슨'),
        ('group', '그룹레슨'),
    )
    personal_or_group = models.CharField(max_length=10,
                                         choices=PERSON_OR_GROUP_CHOICES,
                                         default='personal') # personal or group
    price_of_month = models.IntegerField(default=0)
    preparation = models.TextField(blank=True)
    curriculum_in_first_week = models.TextField(blank=True)
    curriculum_in_second_week = models.TextField(blank=True)
    curriculum_in_third_week = models.TextField(blank=True)
    curriculum_in_fourth_week = models.TextField(blank=True)
    curriculum_in_fifth_week = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('forcompany:index', args=[])

def user_registered_callback(sender, user, request, **kwargs):
    profile = CompanyMasterProfile(user=user)
    profile.company_name = request.POST['company_name']
    profile.local_number = request.POST['local_number']
    profile.phone_number = request.POST['phone_number']
    profile.address = request.POST['address']
    profile.nearby_station = request.POST['nearby_station']
    profile.refund_information = request.POST['refund_information']
    profile.save()

user_registered.connect(user_registered_callback)