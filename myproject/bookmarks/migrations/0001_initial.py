# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bookmark'
        db.create_table(u'bookmarks_bookmark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal(u'bookmarks', ['Bookmark'])

        # Adding model 'Tag'
        db.create_table(u'bookmarks_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'bookmarks', ['Tag'])

        # Adding M2M table for field bookmarks on 'Tag'
        db.create_table(u'bookmarks_tag_bookmarks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'bookmarks.tag'], null=False)),
            ('bookmark', models.ForeignKey(orm[u'bookmarks.bookmark'], null=False))
        ))
        db.create_unique(u'bookmarks_tag_bookmarks', ['tag_id', 'bookmark_id'])


    def backwards(self, orm):
        # Deleting model 'Bookmark'
        db.delete_table(u'bookmarks_bookmark')

        # Deleting model 'Tag'
        db.delete_table(u'bookmarks_tag')

        # Removing M2M table for field bookmarks on 'Tag'
        db.delete_table('bookmarks_tag_bookmarks')


    models = {
        u'bookmarks.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'bookmarks.tag': {
            'Meta': {'object_name': 'Tag'},
            'bookmarks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bookmarks.Bookmark']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['bookmarks']