# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ClickLog.click_url'
        db.alter_column(u'quotes_clicklog', 'click_url', self.gf('django.db.models.fields.URLField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'ClickLog.click_url'
        db.alter_column(u'quotes_clicklog', 'click_url', self.gf('django.db.models.fields.URLField')(max_length=2000))

    models = {
        u'quotes.author': {
            'Meta': {'object_name': 'Author'},
            'amazon_is_referal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amazon_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quotes.Book']", 'symmetrical': 'False', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'goodreads_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'wikipedia_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'quotes.book': {
            'Meta': {'object_name': 'Book'},
            'amazon_is_referal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amazon_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'extended_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'goodreads_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'wikipedia_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'quotes.clicklog': {
            'Meta': {'object_name': 'ClickLog'},
            'click_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'click_destination': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'click_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'click_type_destination_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'click_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'click_user_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quotes.Book']"}),
            'date_added': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_context': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['quotes']