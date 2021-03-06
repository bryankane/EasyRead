# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Source.domain'
        db.alter_column(u'articles_source', 'domain', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=255))
        # Adding unique constraint on 'Source', fields ['domain']
        db.create_unique(u'articles_source', ['domain'])

        # Adding field 'Article.clean_content'
        db.add_column(u'articles_article', 'clean_content',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Source', fields ['domain']
        db.delete_unique(u'articles_source', ['domain'])


        # Changing field 'Source.domain'
        db.alter_column(u'articles_source', 'domain', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))
        # Deleting field 'Article.clean_content'
        db.delete_column(u'articles_article', 'clean_content')


    models = {
        u'articles.article': {
            'Meta': {'unique_together': "(('source', 'title'),)", 'object_name': 'Article'},
            'ari': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'clean_content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'coleman_liau_index': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'flesch': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'flesch_kincaid': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'gunning_fog': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lix': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'rix': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'smog_index': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '6'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Source']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'articles.source': {
            'Meta': {'object_name': 'Source'},
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['articles']