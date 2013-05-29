# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GameDescription.genre'
        db.alter_column(u'gamehub_gamedescription', 'genre', self.gf('django.db.models.fields.CharField')(max_length=3))

    def backwards(self, orm):

        # Changing field 'GameDescription.genre'
        db.alter_column(u'gamehub_gamedescription', 'genre', self.gf('django.db.models.fields.CharField')(max_length=2))

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
            'genre': ('django.db.models.fields.CharField', [], {'default': "'RPG'", 'max_length': '3'}),
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