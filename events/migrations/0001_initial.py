# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'events_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'events', ['User'])

        # Adding model 'Category'
        db.create_table(u'events_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['Category'])

        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default='Cinema', related_name='events', to=orm['events.Category'])),
            ('assistants', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', null=True, to=orm['events.User'])),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'events', ['Event'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'events_user')

        # Deleting model 'Category'
        db.delete_table(u'events_category')

        # Deleting model 'Event'
        db.delete_table(u'events_event')


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
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'null': 'True', 'to': u"orm['events.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['events']