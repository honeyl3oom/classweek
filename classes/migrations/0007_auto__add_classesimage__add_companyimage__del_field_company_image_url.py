# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassesImage'
        db.create_table(u'classes_classesimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classes', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Classes'])),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'classes', ['ClassesImage'])

        # Adding model 'CompanyImage'
        db.create_table(u'classes_companyimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['classes.Company'])),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'classes', ['CompanyImage'])

        # Deleting field 'Company.image_url'
        db.delete_column(u'classes_company', 'image_url')


    def backwards(self, orm):
        # Deleting model 'ClassesImage'
        db.delete_table(u'classes_classesimage')

        # Deleting model 'CompanyImage'
        db.delete_table(u'classes_companyimage')


        # User chose to not deal with backwards NULL issues for 'Company.image_url'
        raise RuntimeError("Cannot reverse this migration. 'Company.image_url' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Company.image_url'
        db.add_column(u'classes_company', 'image_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200),
                      keep_default=False)


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