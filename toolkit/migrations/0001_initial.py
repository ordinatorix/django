# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'toolkit_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'toolkit', ['Category'])

        # Adding model 'System'
        db.create_table(u'toolkit_system', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('categories', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toolkit.Category'])),
            ('purpose', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'toolkit', ['System'])

        # Adding M2M table for field subsystem on 'System'
        m2m_table_name = db.shorten_name(u'toolkit_system_subsystem')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_system', models.ForeignKey(orm[u'toolkit.system'], null=False)),
            ('to_system', models.ForeignKey(orm[u'toolkit.system'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_system_id', 'to_system_id'])

        # Adding model 'Scalar'
        db.create_table(u'toolkit_scalar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
        ))
        db.send_create_signal(u'toolkit', ['Scalar'])

        # Adding model 'Vector'
        db.create_table(u'toolkit_vector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('x_value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('x_angle', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('y_value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('y_angle', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('z_value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('z_angle', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
        ))
        db.send_create_signal(u'toolkit', ['Vector'])

        # Adding model 'Mechanical_Vibration'
        db.create_table(u'toolkit_mechanical_vibration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('initial_force', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Vector'])),
            ('frequency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Scalar'])),
            ('mass', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Scalar'])),
            ('damping_ratio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Scalar'])),
            ('amplitude', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Scalar'])),
            ('modes', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.System'])),
        ))
        db.send_create_signal(u'toolkit', ['Mechanical_Vibration'])

        # Adding model 'Mechanical_Rotation'
        db.create_table(u'toolkit_mechanical_rotation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('torque', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Vector'])),
            ('angular_velocity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', null=True, to=orm['toolkit.Vector'])),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['toolkit.System'], null=True)),
        ))
        db.send_create_signal(u'toolkit', ['Mechanical_Rotation'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'toolkit_category')

        # Deleting model 'System'
        db.delete_table(u'toolkit_system')

        # Removing M2M table for field subsystem on 'System'
        db.delete_table(db.shorten_name(u'toolkit_system_subsystem'))

        # Deleting model 'Scalar'
        db.delete_table(u'toolkit_scalar')

        # Deleting model 'Vector'
        db.delete_table(u'toolkit_vector')

        # Deleting model 'Mechanical_Vibration'
        db.delete_table(u'toolkit_mechanical_vibration')

        # Deleting model 'Mechanical_Rotation'
        db.delete_table(u'toolkit_mechanical_rotation')


    models = {
        u'toolkit.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'toolkit.mechanical_rotation': {
            'Meta': {'object_name': 'Mechanical_Rotation'},
            'angular_velocity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Vector']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toolkit.System']", 'null': 'True'}),
            'torque': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Vector']"}),
            'type_title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'toolkit.mechanical_vibration': {
            'Meta': {'object_name': 'Mechanical_Vibration'},
            'amplitude': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Scalar']"}),
            'damping_ratio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Scalar']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'frequency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Scalar']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_force': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Vector']"}),
            'mass': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.Scalar']"}),
            'modes': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['toolkit.System']"}),
            'type_title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'toolkit.scalar': {
            'Meta': {'object_name': 'Scalar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'})
        },
        u'toolkit.system': {
            'Meta': {'object_name': 'System'},
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['toolkit.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subsystem': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'subsystem_rel_+'", 'null': 'True', 'to': u"orm['toolkit.System']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'toolkit.vector': {
            'Meta': {'object_name': 'Vector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'x_angle': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'x_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'y_angle': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'y_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'z_angle': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'z_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'})
        }
    }

    complete_apps = ['toolkit']