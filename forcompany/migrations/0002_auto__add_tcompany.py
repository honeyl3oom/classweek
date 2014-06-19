# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TCompany'
        db.create_table(u'forcompany_tcompany', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'forcompany', ['TCompany'])


    def backwards(self, orm):
        # Deleting model 'TCompany'
        db.delete_table(u'forcompany_tcompany')


    models = {
        u'forcompany.companyinfo': {
            'Meta': {'ordering': "('id',)", 'object_name': 'CompanyInfo'},
            'class1_count': ('django.db.models.fields.TextField', [], {}),
            'class1_price': ('django.db.models.fields.TextField', [], {}),
            'class2_count': ('django.db.models.fields.TextField', [], {}),
            'class2_price': ('django.db.models.fields.TextField', [], {}),
            'class3_count': ('django.db.models.fields.TextField', [], {}),
            'class3_price': ('django.db.models.fields.TextField', [], {}),
            'class4_count': ('django.db.models.fields.TextField', [], {}),
            'class4_price': ('django.db.models.fields.TextField', [], {}),
            'class5_count': ('django.db.models.fields.TextField', [], {}),
            'class5_price': ('django.db.models.fields.TextField', [], {}),
            'class6_count': ('django.db.models.fields.TextField', [], {}),
            'class6_price': ('django.db.models.fields.TextField', [], {}),
            'curriculum1_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum1_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum1_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum1_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum2_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum2_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum2_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum2_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum3_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum3_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum3_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum3_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum4_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum4_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum4_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum4_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum5_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum5_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum5_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum5_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum6_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum6_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum6_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum6_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum7_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum7_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum7_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum7_time': ('django.db.models.fields.TextField', [], {}),
            'curriculum8_class_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum8_class_detail_description': ('django.db.models.fields.TextField', [], {}),
            'curriculum8_preparation_material': ('django.db.models.fields.TextField', [], {}),
            'curriculum8_time': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'facility': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nearby_station': ('django.db.models.fields.TextField', [], {}),
            'position': ('django.db.models.fields.TextField', [], {}),
            'preparation_material': ('django.db.models.fields.TextField', [], {}),
            'refund_info': ('django.db.models.fields.TextField', [], {}),
            'teacher_career': ('django.db.models.fields.TextField', [], {}),
            'teacher_name': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'forcompany.tcompany': {
            'Meta': {'object_name': 'TCompany'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['forcompany']