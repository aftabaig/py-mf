# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Branch'
        db.create_table(u'meta_branch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('emailAddress', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('weekdayTimings', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('saturdayTimings', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 3, 0, 0), auto_now=True, auto_now_add=True, blank=True)),
            ('updatedAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 3, 0, 0), auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'meta', ['Branch'])

        # Adding model 'Contact'
        db.create_table(u'meta_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('jobRole', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['meta.Branch'])),
            ('contactNumber', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('mobileNumber', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('emailAddress', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('profileImageUrl', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 3, 0, 0), auto_now=True, auto_now_add=True, blank=True)),
            ('updatedAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 3, 0, 0), auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'meta', ['Contact'])

        # Adding model 'Deal'
        db.create_table(u'meta_deal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('availability', self.gf('django.db.models.fields.DateTimeField')()),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('availableOnline', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dealImageUrl', self.gf('django.db.models.fields.CharField')(max_length=1024, blank=True)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 3, 0, 0), auto_now=True, auto_now_add=True, blank=True)),
            ('updatedAt', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 3, 0, 0), auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'meta', ['Deal'])

        # Adding model 'DealBranch'
        db.create_table(u'meta_dealbranch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meta.Branch'])),
            ('deal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meta.Deal'])),
        ))
        db.send_create_signal(u'meta', ['DealBranch'])


    def backwards(self, orm):
        # Deleting model 'Branch'
        db.delete_table(u'meta_branch')

        # Deleting model 'Contact'
        db.delete_table(u'meta_contact')

        # Deleting model 'Deal'
        db.delete_table(u'meta_deal')

        # Deleting model 'DealBranch'
        db.delete_table(u'meta_dealbranch')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'meta.branch': {
            'Meta': {'object_name': 'Branch'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'saturdayTimings': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'updatedAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'weekdayTimings': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'meta.contact': {
            'Meta': {'object_name': 'Contact'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['meta.Branch']"}),
            'contactNumber': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'emailAddress': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobRole': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'mobileNumber': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profileImageUrl': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'updatedAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'meta.deal': {
            'Meta': {'object_name': 'Deal'},
            'availability': ('django.db.models.fields.DateTimeField', [], {}),
            'availableOnline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'dealImageUrl': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'updatedAt': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 3, 0, 0)', 'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'meta.dealbranch': {
            'Meta': {'object_name': 'DealBranch'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meta.Branch']"}),
            'deal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meta.Deal']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['meta']