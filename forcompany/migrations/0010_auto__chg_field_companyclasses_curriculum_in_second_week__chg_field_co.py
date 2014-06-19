# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CompanyClasses.curriculum_in_second_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_second_week', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'CompanyClasses.curriculum_in_fourth_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_fourth_week', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'CompanyClasses.preparation'
        db.alter_column(u'forcompany_companyclasses', 'preparation', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'CompanyClasses.curriculum_in_fifth_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_fifth_week', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'CompanyClasses.curriculum_in_first_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_first_week', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'CompanyClasses.curriculum_in_third_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_third_week', self.gf('django.db.models.fields.TextField')(default=''))

    def backwards(self, orm):

        # Changing field 'CompanyClasses.curriculum_in_second_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_second_week', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CompanyClasses.curriculum_in_fourth_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_fourth_week', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CompanyClasses.preparation'
        db.alter_column(u'forcompany_companyclasses', 'preparation', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CompanyClasses.curriculum_in_fifth_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_fifth_week', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CompanyClasses.curriculum_in_first_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_first_week', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CompanyClasses.curriculum_in_third_week'
        db.alter_column(u'forcompany_companyclasses', 'curriculum_in_third_week', self.gf('django.db.models.fields.TextField')(null=True))

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
        u'classes.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'})
        },
        u'classes.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'get_subcategorys'", 'to': u"orm['classes.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'name_kor': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'order_priority_number': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'forcompany.companyclasses': {
            'Meta': {'object_name': 'CompanyClasses'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'curriculum_in_fifth_week': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'curriculum_in_first_week': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'curriculum_in_fourth_week': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'curriculum_in_second_week': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'curriculum_in_third_week': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'personal_or_group': ('django.db.models.fields.CharField', [], {'default': "'personal'", 'max_length': '10'}),
            'preparation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'price_of_month': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sub_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['classes.SubCategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'forcompany.companymasterprofile': {
            'Meta': {'object_name': 'CompanyMasterProfile'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nearby_station': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'refund_information': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'master_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['forcompany']