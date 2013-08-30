# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'quotes_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_text', self.gf('django.db.models.fields.TextField')()),
            ('quote_context', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quotes.Book'])),
        ))
        db.send_create_signal(u'quotes', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'quotes_quote')


    models = {
        u'quotes.author': {
            'Meta': {'object_name': 'Author'},
            'amazon_is_referal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amazon_url': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quotes.Book']", 'symmetrical': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'goodreads_url': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'wikipedia_url': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'})
        },
        u'quotes.book': {
            'Meta': {'object_name': 'Book'},
            'amazon_is_referal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amazon_url': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            'extended_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'goodreads_url': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'wikipedia_url': ('django.db.models.fields.TextField', [], {'max_length': '2000', 'blank': 'True'})
        },
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quotes.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_context': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['quotes']