# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Classes.preparation'
        db.alter_column(u'classes_classes', 'preparation', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Classes.zone'
        db.alter_column(u'classes_classes', 'zone', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Classes.title'
        db.alter_column(u'classes_classes', 'title', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Classes.countOfMonth'
        db.alter_column(u'classes_classes', 'countOfMonth', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Classes.priceOfDay'
        db.alter_column(u'classes_classes', 'priceOfDay', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Classes.personalOfGroup'
        db.alter_column(u'classes_classes', 'personalOfGroup', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Classes.short_description'
        db.alter_column(u'classes_classes', 'short_description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Classes.refundInfomation'
        db.alter_column(u'classes_classes', 'refundInfomation', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Classes.priceOfMonth'
        db.alter_column(u'classes_classes', 'priceOfMonth', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Classes.countOfDay'
        db.alter_column(u'classes_classes', 'countOfDay', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Classes.description'
        db.alter_column(u'classes_classes', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Classes.preparation'
        raise RuntimeError("Cannot reverse this migration. 'Classes.preparation' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.preparation'
        db.alter_column(u'classes_classes', 'preparation', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Classes.zone'
        raise RuntimeError("Cannot reverse this migration. 'Classes.zone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.zone'
        db.alter_column(u'classes_classes', 'zone', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Classes.title'
        raise RuntimeError("Cannot reverse this migration. 'Classes.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.title'
        db.alter_column(u'classes_classes', 'title', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Classes.countOfMonth'
        raise RuntimeError("Cannot reverse this migration. 'Classes.countOfMonth' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.countOfMonth'
        db.alter_column(u'classes_classes', 'countOfMonth', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Classes.priceOfDay'
        raise RuntimeError("Cannot reverse this migration. 'Classes.priceOfDay' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.priceOfDay'
        db.alter_column(u'classes_classes', 'priceOfDay', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Classes.personalOfGroup'
        raise RuntimeError("Cannot reverse this migration. 'Classes.personalOfGroup' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.personalOfGroup'
        db.alter_column(u'classes_classes', 'personalOfGroup', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Classes.short_description'
        raise RuntimeError("Cannot reverse this migration. 'Classes.short_description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.short_description'
        db.alter_column(u'classes_classes', 'short_description', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Classes.refundInfomation'
        raise RuntimeError("Cannot reverse this migration. 'Classes.refundInfomation' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.refundInfomation'
        db.alter_column(u'classes_classes', 'refundInfomation', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'Classes.priceOfMonth'
        raise RuntimeError("Cannot reverse this migration. 'Classes.priceOfMonth' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.priceOfMonth'
        db.alter_column(u'classes_classes', 'priceOfMonth', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Classes.countOfDay'
        raise RuntimeError("Cannot reverse this migration. 'Classes.countOfDay' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.countOfDay'
        db.alter_column(u'classes_classes', 'countOfDay', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Classes.description'
        raise RuntimeError("Cannot reverse this migration. 'Classes.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Classes.description'
        db.alter_column(u'classes_classes', 'description', self.gf('django.db.models.fields.TextField')())

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
            'personalOfGroup': ('django.db.models.fields.TextField', [], {'null': 'True'}),
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