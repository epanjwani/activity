# Generated by Django 2.2.10 on 2020-05-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formlibrary', '0006_auto_20200519_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='construction',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='distribution',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ('name',)},
        ),
    ]
