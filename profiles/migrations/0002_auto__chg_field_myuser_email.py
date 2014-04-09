# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MyUser.email'
        db.alter_column(u'profiles_myuser', 'email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75))

    def backwards(self, orm):

        # Changing field 'MyUser.email'
        db.alter_column(u'profiles_myuser', 'email', self.gf('django.db.models.fields.EmailField')(max_length=255, unique=True))

    models = {
        u'profiles.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['profiles']