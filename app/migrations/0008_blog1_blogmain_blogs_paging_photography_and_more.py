# Generated by Django 5.1.2 on 2024-10-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_abouttext1_list1_remove_abouttext1_list2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description1', models.CharField(blank=True, max_length=500, null=True)),
                ('description2', models.CharField(blank=True, max_length=500, null=True)),
                ('description3', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('link_url1', models.URLField(max_length=255)),
                ('link_name1', models.CharField(max_length=255)),
                ('link_url2', models.URLField(max_length=255)),
                ('link_name2', models.CharField(max_length=255)),
                ('post', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url3', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name3', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url4', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name4', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog1')),
                ('link_url5', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name5', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Blog1',
                'verbose_name_plural': 'Blog1',
            },
        ),
        migrations.CreateModel(
            name='BlogMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Blog Main',
                'verbose_name_plural': 'Blog Main',
            },
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description1', models.CharField(blank=True, max_length=500, null=True)),
                ('description2', models.CharField(blank=True, max_length=500, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs')),
                ('post', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url1', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name1', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url2', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name2', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url3', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name3', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Blogs',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Paging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(max_length=255)),
                ('link_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Paging',
                'verbose_name_plural': 'Paging',
            },
        ),
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photography.url')),
            ],
            options={
                'verbose_name': 'Photography',
                'verbose_name_plural': 'Photography',
            },
        ),
        migrations.CreateModel(
            name='PortfolioMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Portfolio Main',
                'verbose_name_plural': 'Portfolio Main',
            },
        ),
        migrations.CreateModel(
            name='PrintMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='print_media.url')),
            ],
            options={
                'verbose_name': 'Print Media',
                'verbose_name_plural': 'Print Media',
            },
        ),
        migrations.CreateModel(
            name='WebImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image_title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='web_image.url')),
            ],
            options={
                'verbose_name': 'Web Image',
                'verbose_name_plural': 'Web Image',
            },
        ),
    ]
