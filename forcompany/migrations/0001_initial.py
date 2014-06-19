# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompanyInfo'
        db.create_table(u'forcompany_companyinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('position', self.gf('django.db.models.fields.TextField')()),
            ('nearby_station', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('facility', self.gf('django.db.models.fields.TextField')()),
            ('class1_count', self.gf('django.db.models.fields.TextField')()),
            ('class1_price', self.gf('django.db.models.fields.TextField')()),
            ('class2_count', self.gf('django.db.models.fields.TextField')()),
            ('class2_price', self.gf('django.db.models.fields.TextField')()),
            ('class3_count', self.gf('django.db.models.fields.TextField')()),
            ('class3_price', self.gf('django.db.models.fields.TextField')()),
            ('class4_count', self.gf('django.db.models.fields.TextField')()),
            ('class4_price', self.gf('django.db.models.fields.TextField')()),
            ('class5_count', self.gf('django.db.models.fields.TextField')()),
            ('class5_price', self.gf('django.db.models.fields.TextField')()),
            ('class6_count', self.gf('django.db.models.fields.TextField')()),
            ('class6_price', self.gf('django.db.models.fields.TextField')()),
            ('teacher_name', self.gf('django.db.models.fields.TextField')()),
            ('teacher_career', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('refund_info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'forcompany', ['CompanyInfo'])


    def backwards(self, orm):
        # Deleting model 'CompanyInfo'
        db.delete_table(u'forcompany_companyinfo')


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
        }
    }

    complete_apps = ['forcompany']