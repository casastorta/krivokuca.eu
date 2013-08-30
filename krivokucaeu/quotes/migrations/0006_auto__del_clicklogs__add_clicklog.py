# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ClickLogs'
        db.delete_table(u'quotes_clicklogs')

        # Adding model 'ClickLog'
        db.create_table(u'quotes_clicklog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('click_url', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('click_type', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('click_destination', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('click_type_destination_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('click_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('click_user_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
        ))
        db.send_create_signal(u'quotes', ['ClickLog'])


    def backwards(self, orm):
        # Adding model 'ClickLogs'
        db.create_table(u'quotes_clicklogs', (
            ('click_url', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('click_user_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('click_destination', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('click_type', self.gf('django.db.models.fields.CharField')(max_length=4)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('click_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('click_type_destination_id', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'quotes', ['ClickLogs'])

        # Deleting model 'ClickLog'
        db.delete_table(u'quotes_clicklog')


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
            'click_url': ('django.db.models.fields.TextField', [], {'max_length': '2000'}),
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