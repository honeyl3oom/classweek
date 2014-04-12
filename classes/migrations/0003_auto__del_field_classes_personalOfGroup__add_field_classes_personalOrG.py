# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Classes.personalOfGroup'
        db.delete_column(u'classes_classes', 'personalOfGroup')

        # Adding field 'Classes.personalOrGroup'
        db.add_column(u'classes_classes', 'personalOrGroup',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Classes.personalOfGroup'
        db.add_column(u'classes_classes', 'personalOfGroup',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Deleting field 'Classes.personalOrGroup'
        db.delete_column(u'classes_classes', 'personalOrGroup')


    models = {
        u'classes.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'classes.classes': {
            'Meta': {'object_name': 'Classes'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Company']"}),
            'countOfDay': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'countOfMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personalOrGroup': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'preparation': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'priceOfDay': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'priceOfMonth': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'refundInfomation': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'subCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.SubCategory']"}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'zone': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'classes.company': {
            'Meta': {'object_name': 'Company'},
            'facilitiesInfomation': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'nearby_station': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'phonenumber': ('django.db.models.fields.TextField', [], {})
        },
        u'classes.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'classes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Classes']"}),
            'dayOfWeek': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'startTime': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'classes.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['classes']