# Generated by Django 3.1.7 on 2021-03-07 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlist', '0002_auto_20210307_1910'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activities',
            new_name='Activitie',
        ),
        migrations.RenameModel(
            old_name='Country',
            new_name='Countrie',
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
        migrations.RenameModel(
            old_name='MemberActivities',
            new_name='MemberActivitie',
        ),
        migrations.RenameModel(
            old_name='MemberComitees',
            new_name='MemberComitee',
        ),
        migrations.RenameModel(
            old_name='MemberStatus',
            new_name='MemberStatuse',
        ),
        migrations.RenameModel(
            old_name='RelationshipStatus',
            new_name='RelationshipStatuse',
        ),
    ]
