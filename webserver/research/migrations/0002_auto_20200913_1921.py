# Generated by Django 3.0.3 on 2020-09-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ai_table',
            name='id',
        ),
        migrations.RemoveField(
            model_name='indicator_table',
            name='id',
        ),
        migrations.RemoveField(
            model_name='stock_table',
            name='id',
        ),
        migrations.AlterField(
            model_name='ai_table',
            name='AI_Name',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='indicator_table',
            name='indicator_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock_table',
            name='Stock_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock_table',
            name='Stock_open',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='stock_table',
            name='Stock_vol',
            field=models.IntegerField(blank=True),
        ),
    ]
