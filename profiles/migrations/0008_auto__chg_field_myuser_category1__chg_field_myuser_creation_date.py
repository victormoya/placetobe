# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MyUser.category1'
        db.alter_column(u'profiles_myuser', 'category1_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['events.Category']))

        # Changing field 'MyUser.creation_date'
        db.alter_column(u'profiles_myuser', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 2, 13, 0, 0)))

    def backwards(self, orm):

        # Changing field 'MyUser.category1'
        db.alter_column(u'profiles_myuser', 'category1_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Category']))

        # Changing field 'MyUser.creation_date'
        db.alter_column(u'profiles_myuser', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

    models = {
        u'events.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'profiles.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'category1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'profile'", 'null': 'True', 'to': u"orm['events.Category']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['profiles']