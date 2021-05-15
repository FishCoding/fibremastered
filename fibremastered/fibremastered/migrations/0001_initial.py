# Generated by Django 3.2.3 on 2021-05-14 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('template_path', models.CharField(help_text='Format: app/template_name.html', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('display_title', models.CharField(max_length=250)),
                ('title_text', models.CharField(blank=True, max_length=250)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=100)),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fibremastered.template')),
            ],
        ),
    ]