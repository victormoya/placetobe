# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.username'
        db.delete_column(u'events_user', 'username')

        # Deleting field 'User.email'
        db.delete_column(u'events_user', 'email')

        # Adding field 'User.last_login'
        db.add_column(u'events_user', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


        # Changing field 'User.password'
        db.alter_column(u'events_user', 'password', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Adding field 'User.username'
        db.add_column(u'events_user', 'username',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=50),
                      keep_default=False)

        # Adding field 'User.email'
        db.add_column(u'events_user', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='a@mail.com', max_length=75),
                      keep_default=False)

        # Deleting field 'User.last_login'
        db.delete_column(u'events_user', 'last_login')


        # Changing field 'User.password'
        db.alter_column(u'events_user', 'password', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'events.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'assistants': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': "'Cinema'", 'related_name': "'events'", 'to': u"orm['events.Category']"}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'null': 'True', 'to': u"orm['events.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['events']