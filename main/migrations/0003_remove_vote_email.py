# Generated by Django 4.0.10 on 2023-06-16 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_vote_range1_alter_vote_range2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='email',
        ),
    ]
