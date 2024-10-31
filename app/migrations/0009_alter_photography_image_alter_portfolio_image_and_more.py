# Generated by Django 5.1.2 on 2024-10-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blog1_blogmain_blogs_paging_photography_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photography',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photography'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='printmedia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='print_media'),
        ),
        migrations.AlterField(
            model_name='stories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='stories'),
        ),
        migrations.AlterField(
            model_name='webimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='web_image'),
        ),
    ]