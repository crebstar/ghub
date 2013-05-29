# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'gamehub_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('age_limit', self.gf('django.db.models.fields.IntegerField')(default=18)),
        ))
        db.send_create_signal(u'gamehub', ['Game'])

        # Adding model 'GameDescription'
        db.create_table(u'gamehub_gamedescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gamehub.Game'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('genre', self.gf('django.db.models.fields.CharField')(default='RPG', max_length=2)),
        ))
        db.send_create_signal(u'gamehub', ['GameDescription'])

        # Adding model 'GameReview'
        db.create_table(u'gamehub_gamereview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gamehub.Game'])),
            ('reviewDescription', self.gf('django.db.models.fields.CharField')(default='', max_length=500)),
            ('reviewTitle', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'gamehub', ['GameReview'])

        # Adding model 'GameRating'
        db.create_table(u'gamehub_gamerating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gameReview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gamehub.GameReview'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=3)),
        ))
        db.send_create_signal(u'gamehub', ['GameRating'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'gamehub_game')

        # Deleting model 'GameDescription'
        db.delete_table(u'gamehub_gamedescription')

        # Deleting model 'GameReview'
        db.delete_table(u'gamehub_gamereview')

        # Deleting model 'GameRating'
        db.delete_table(u'gamehub_gamerating')


    models = {
        u'gamehub.game': {
            'Meta': {'object_name': 'Game'},
            'age_limit': ('django.db.models.fields.IntegerField', [], {'default': '18'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'gamehub.gamedescription': {
            'Meta': {'object_name': 'GameDescription'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gamehub.Game']"}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "'RPG'", 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'gamehub.gamerating': {
            'Meta': {'object_name': 'GameRating'},
            'gameReview': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gamehub.GameReview']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'gamehub.gamereview': {
            'Meta': {'object_name': 'GameReview'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gamehub.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewDescription': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'reviewTitle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['gamehub']