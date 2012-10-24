# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hall'
        db.create_table('halls_hall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lon', self.gf('django.db.models.fields.FloatField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('halls', ['Hall'])

        # Adding model 'Hour'
        db.create_table('halls_hour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host_hall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halls.Hall'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('start_hour', self.gf('django.db.models.fields.IntegerField')()),
            ('start_minute', self.gf('django.db.models.fields.IntegerField')()),
            ('end_hour', self.gf('django.db.models.fields.IntegerField')()),
            ('end_minute', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('halls', ['Hour'])

        # Adding model 'MealMenu'
        db.create_table('halls_mealmenu', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meal_time', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halls.Hour'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('halls', ['MealMenu'])

        # Adding model 'FoodCategory'
        db.create_table('halls_foodcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('halls', ['FoodCategory'])

        # Adding model 'FoodAttribute'
        db.create_table('halls_foodattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('halls', ['FoodAttribute'])

        # Adding model 'FoodItem'
        db.create_table('halls_fooditem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halls.FoodCategory'], null=True, blank=True)),
        ))
        db.send_create_signal('halls', ['FoodItem'])

        # Adding M2M table for field meal_menu on 'FoodItem'
        db.create_table('halls_fooditem_meal_menu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fooditem', models.ForeignKey(orm['halls.fooditem'], null=False)),
            ('mealmenu', models.ForeignKey(orm['halls.mealmenu'], null=False))
        ))
        db.create_unique('halls_fooditem_meal_menu', ['fooditem_id', 'mealmenu_id'])

        # Adding M2M table for field attributes on 'FoodItem'
        db.create_table('halls_fooditem_attributes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fooditem', models.ForeignKey(orm['halls.fooditem'], null=False)),
            ('foodattribute', models.ForeignKey(orm['halls.foodattribute'], null=False))
        ))
        db.create_unique('halls_fooditem_attributes', ['fooditem_id', 'foodattribute_id'])


    def backwards(self, orm):
        # Deleting model 'Hall'
        db.delete_table('halls_hall')

        # Deleting model 'Hour'
        db.delete_table('halls_hour')

        # Deleting model 'MealMenu'
        db.delete_table('halls_mealmenu')

        # Deleting model 'FoodCategory'
        db.delete_table('halls_foodcategory')

        # Deleting model 'FoodAttribute'
        db.delete_table('halls_foodattribute')

        # Deleting model 'FoodItem'
        db.delete_table('halls_fooditem')

        # Removing M2M table for field meal_menu on 'FoodItem'
        db.delete_table('halls_fooditem_meal_menu')

        # Removing M2M table for field attributes on 'FoodItem'
        db.delete_table('halls_fooditem_attributes')


    models = {
        'halls.foodattribute': {
            'Meta': {'object_name': 'FoodAttribute'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'halls.foodcategory': {
            'Meta': {'object_name': 'FoodCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'halls.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['halls.FoodAttribute']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halls.FoodCategory']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meal_menu': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['halls.MealMenu']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
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