# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'classes_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('phonenumber', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('nearby_station', self.gf('django.db.models.fields.TextField')(null=True)),
            ('facilitiesInfomation', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'classes', ['Company'])

        # Adding model 'CompanyImage'
        db.create_table(u'classes_companyimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Company'])),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'classes', ['CompanyImage'])

        # Adding model 'Category'
        db.create_table(u'classes_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
        ))
        db.send_create_signal(u'classes', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'classes_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Category'])),
        ))
        db.send_create_signal(u'classes', ['SubCategory'])

        # Adding model 'Classes'
        db.create_table(u'classes_classes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('subCategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.SubCategory'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Company'])),
            ('short_description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('preparation', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('zone', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('personalOrGroup', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('refundInfomation', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('priceOfDay', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('countOfMonth', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('priceOfMonth', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal(u'classes', ['Classes'])

        # Adding model 'ClassesImage'
        db.create_table(u'classes_classesimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Classes'])),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'classes', ['ClassesImage'])

        # Adding model 'Schedule'
        db.create_table(u'classes_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Classes'])),
            ('dayOfWeek', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('startTime', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'classes', ['Schedule'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'classes_company')

        # Deleting model 'CompanyImage'
        db.delete_table(u'classes_companyimage')

        # Deleting model 'Category'
        db.delete_table(u'classes_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'classes_subcategory')

        # Deleting model 'Classes'
        db.delete_table(u'classes_classes')

        # Deleting model 'ClassesImage'
        db.delete_table(u'classes_classesimage')

        # Deleting model 'Schedule'
        db.delete_table(u'classes_schedule')


    models = {
        u'classes.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'classes.classes': {
            'Meta': {'object_name': 'Classes'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Company']"}),
            'countOfMonth': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personalOrGroup': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'preparation': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'priceOfDay': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'priceOfMonth': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'refundInfomation': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'subCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.SubCategory']"}),
            'title': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'zone': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        u'classes.classesimage': {
            'Meta': {'object_name': 'ClassesImage'},
            'classes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Classes']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'classes.company': {
            'Meta': {'object_name': 'Company'},
            'facilitiesInfomation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'nearby_station': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'phonenumber': ('django.db.models.fields.TextField', [], {})
        },
        u'classes.companyimage': {
            'Meta': {'object_name': 'CompanyImage'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'classes.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'classes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Classes']"}),
            'dayOfWeek': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'startTime': ('django.db.models.fields.TimeField', [], {})
        },
        u'classes.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['classes']