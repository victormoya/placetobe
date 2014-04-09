# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'comments_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.MyUser'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['events.Event'])),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=512)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'comments', ['Comment'])

        # Adding model 'Voter'
        db.create_table(u'comments_voter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votes', to=orm['profiles.MyUser'])),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='voters', to=orm['comments.Comment'])),
            ('vote', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'comments', ['Voter'])

        # Adding unique constraint on 'Voter', fields ['user', 'comment']
        db.create_unique(u'comments_voter', ['user_id', 'comment_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Voter', fields ['user', 'comment']
        db.delete_unique(u'comments_voter', ['user_id', 'comment_id'])

        # Deleting model 'Comment'
        db.delete_table(u'comments_comment')

        # Deleting model 'Voter'
        db.delete_table(u'comments_voter')


    models = {
        u'comments.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.MyUser']"}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'comments.voter': {
            'Meta': {'unique_together': "(('user', 'comment'),)", 'object_name': 'Voter'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'voters'", 'to': u"orm['comments.Comment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': u"orm['profiles.MyUser']"}),
            'vote': ('django.db.models.fields.IntegerField', [], {})
        },
        u'events.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': "'General'", 'related_name': "'events'", 'to': u"orm['events.Category']"}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '175'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'null': 'True', 'to': u"orm['profiles.MyUser']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'category1': ('django.db.models.fields.related.ForeignKey', [], {'default': "'Art'", 'related_name': "'profile'", 'null': 'True', 'blank': 'True', 'to': u"orm['events.Category']"}),
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

    complete_apps = ['comments']