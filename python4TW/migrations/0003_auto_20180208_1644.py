# Generated by Django 2.0.2 on 2018-02-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python4TW', '0002_ingredient_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='carbohydrates',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='energy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='fat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='protein',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='salt',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='saturated',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='sugar',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]