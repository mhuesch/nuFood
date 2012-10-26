# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'FoodCategory'
        db.delete_table('halls_foodcategory')

        # Adding unique constraint on 'FoodAttribute', fields ['name']
        db.create_unique('halls_foodattribute', ['name'])

        # Deleting field 'FoodItem.category'
        db.delete_column('halls_fooditem', 'category_id')

        # Adding unique constraint on 'FoodItem', fields ['name']
        db.create_unique('halls_fooditem', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'FoodItem', fields ['name']
        db.delete_unique('halls_fooditem', ['name'])

        # Removing unique constraint on 'FoodAttribute', fields ['name']
        db.delete_unique('halls_foodattribute', ['name'])

        # Adding model 'FoodCategory'
        db.create_table('halls_foodcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('halls', ['FoodCategory'])

        # Adding field 'FoodItem.category'
        db.add_column('halls_fooditem', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['halls.FoodCategory'], null=True, blank=True),
                      keep_default=False)


    models = {
        'halls.foodattribute': {
            'Meta': {'object_name': 'FoodAttribute'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'halls.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': "orm['halls.FoodAttribute']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_menu': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['halls.MealMenu']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'halls.hall': {
            'Meta': {'object_name': 'Hall'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'halls.hour': {
            'Meta': {'object_name': 'Hour'},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            'end_hour': ('django.db.models.fields.IntegerField', [], {}),
            'end_minute': ('django.db.models.fields.IntegerField', [], {}),
            'host_hall': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halls.Hall']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'start_hour': ('django.db.models.fields.IntegerField', [], {}),
            'start_minute': ('django.db.models.fields.IntegerField', [], {})
        },
        'halls.mealmenu': {
            'Meta': {'object_name': 'MealMenu'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_time': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halls.Hour']"})
        }
    }

    complete_apps = ['halls']