# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TCompany'
        db.delete_table(u'forcompany_tcompany')

        # Deleting model 'CompanyInfo'
        db.delete_table(u'forcompany_companyinfo')

        # Adding model 'CompanyMasterProfile'
        db.create_table(u'forcompany_companymasterprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('company_name', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('local_number', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone_number', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('nearby_station', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('refund_information', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'forcompany', ['CompanyMasterProfile'])


    def backwards(self, orm):
        # Adding model 'TCompany'
        db.create_table(u'forcompany_tcompany', (
            ('name', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'forcompany', ['TCompany'])

        # Adding model 'CompanyInfo'
        db.create_table(u'forcompany_companyinfo', (
            ('curriculum7_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_class_description', self.gf('django.db.models.fields.TextField')()),
            ('facility', self.gf('django.db.models.fields.TextField')()),
            ('class2_price', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_class_description', self.gf('django.db.models.fields.TextField')()),
            ('class4_count', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('class1_price', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('class6_price', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_time', self.gf('django.db.models.fields.TextField')()),
            ('class1_count', self.gf('django.db.models.fields.TextField')()),
            ('class6_count', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('refund_info', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_time', self.gf('django.db.models.fields.TextField')()),
            ('class3_count', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_time', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum5_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum8_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('class2_count', self.gf('django.db.models.fields.TextField')()),
            ('class5_price', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nearby_station', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_time', self.gf('django.db.models.fields.TextField')()),
            ('class5_count', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('preparation_material', self.gf('django.db.models.fields.TextField')()),
            ('teacher_name', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum7_class_description', self.gf('django.db.models.fields.TextField')()),
            ('class3_price', self.gf('django.db.models.fields.TextField')()),
            ('teacher_career', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('class4_price', self.gf('django.db.models.fields.TextField')()),
            ('curriculum1_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('curriculum4_class_detail_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum6_class_description', self.gf('django.db.models.fields.TextField')()),
            ('curriculum2_class_description', self.gf('django.db.models.fields.TextField')()),
            ('position', self.gf('django.db.models.fields.TextField')()),
            ('curriculum3_preparation_material', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'forcompany', ['CompanyInfo'])

        # Deleting model 'CompanyMasterProfile'
        db.delete_table(u'forcompany_companymasterprofile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forcompany.companymasterprofile': {
            'Meta': {'object_name': 'CompanyMasterProfile'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'company_name': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_number': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nearby_station': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'refund_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['forcompany']