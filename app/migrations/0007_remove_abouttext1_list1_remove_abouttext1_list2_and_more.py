# Generated by Django 4.2.13 on 2024-10-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_abouttext1_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abouttext1',
            name='list1',
        ),
        migrations.RemoveField(
            model_name='abouttext1',
            name='list2',
        ),
        migrations.RemoveField(
            model_name='abouttext1',
            name='list3',
        ),
        migrations.RemoveField(
            model_name='abouttext1',
            name='list4',
        ),
        migrations.RemoveField(
            model_name='abouttext1',
            name='list5',
        ),
        migrations.AddField(
            model_name='abouttext2',
            name='text',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='abouttext2',
            name='blockquote',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='abouttext2',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
