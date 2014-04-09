# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MyUser.date_of_birth'
        db.delete_column(u'profiles_myuser', 'date_of_birth')

        # Adding field 'MyUser.creation_date'
        db.add_column(u'profiles_myuser', 'creation_date',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MyUser.date_of_birth'
        db.add_column(u'profiles_myuser', 'date_of_birth',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Deleting field 'MyUser.creation_date'
        db.delete_column(u'profiles_myuser', 'creation_date')


    models = {
        u'profiles.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'creation_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['profiles']