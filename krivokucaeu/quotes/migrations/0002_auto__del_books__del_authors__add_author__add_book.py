# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Books'
        db.delete_table(u'quotes_books')

        # Deleting model 'Authors'
        db.delete_table(u'quotes_authors')

        # Removing M2M table for field books on 'Authors'
        db.delete_table(db.shorten_name(u'quotes_authors_books'))

        # Adding model 'Author'
        db.create_table(u'quotes_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('amazon_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('amazon_is_referal', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wikipedia_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('goodreads_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('short_bio', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'quotes', ['Author'])

        # Adding M2M table for field books on 'Author'
        m2m_table_name = db.shorten_name(u'quotes_author_books')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(orm[u'quotes.author'], null=False)),
            ('book', models.ForeignKey(orm[u'quotes.book'], null=False))
        ))
        db.create_unique(m2m_table_name, ['author_id', 'book_id'])

        # Adding model 'Book'
        db.create_table(u'quotes_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('extended_title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('amazon_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('amazon_is_referal', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wikipedia_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('goodreads_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'quotes', ['Book'])


    def backwards(self, orm):
        # Adding model 'Books'
        db.create_table(u'quotes_books', (
            ('amazon_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('wikipedia_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('amazon_is_referal', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('extended_title', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('goodreads_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'quotes', ['Books'])

        # Adding model 'Authors'
        db.create_table(u'quotes_authors', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('amazon_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('wikipedia_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            ('amazon_is_referal', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('short_bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('goodreads_url', self.gf('django.db.models.fields.TextField')(max_length=2000, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'quotes', ['Authors'])

        # Adding M2M table for field books on 'Authors'
        m2m_table_name = db.shorten_name(u'quotes_authors_books')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('authors', models.ForeignKey(orm[u'quotes.authors'], null=False)),
            ('books', models.ForeignKey(orm[u'quotes.books'], null=False))
        ))
        db.create_unique(m2m_table_name, ['authors_id', 'books_id'])

        # Deleting model 'Author'
        db.delete_table(u'quotes_author')

        # Removing M2M table for field books on 'Author'
        db.delete_table(db.shorten_name(u'quotes_author_books'))

        # Deleting model 'Book'
        db.delete_table(u'quotes_book')


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
        }
    }

    complete_apps = ['quotes']