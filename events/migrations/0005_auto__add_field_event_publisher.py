# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.publisher'
        db.add_column(u'events_event', 'publisher',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', null=True, to=orm['profiles.MyUser']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.publisher'
        db.delete_column(u'events_event', 'publisher_id')


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
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'null': 'True', 'to': u"orm['profiles.MyUser']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['events']