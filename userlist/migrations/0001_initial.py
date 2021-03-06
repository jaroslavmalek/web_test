# Generated by Django 3.1.7 on 2021-03-07 16:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('mid_name', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=10)),
                ('postal_place', models.CharField(max_length=255)),
                ('occupation', models.CharField(blank=True, max_length=255)),
                ('phone_home', models.CharField(blank=True, max_length=20)),
                ('phone_work', models.CharField(blank=True, max_length=20)),
                ('phone_cell', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('born', models.DateField()),
                ('birthplace', models.CharField(max_length=40)),
                ('baptised', models.DateField(blank=True, null=True)),
                ('baptised_place', models.CharField(blank=True, max_length=40)),
                ('confirmation', models.DateField(blank=True, null=True)),
                ('confirmation_place', models.CharField(blank=True, max_length=40)),
                ('confirmation_hnr', models.CharField(blank=True, max_length=16)),
                ('father_id', models.IntegerField(blank=True, default=0)),
                ('father', models.TextField(blank=True)),
                ('mother_id', models.IntegerField(blank=True, default=0)),
                ('mother', models.TextField(blank=True)),
                ('relation_status', models.CharField(choices=[('U', 'Ugift'), ('G', 'Gift'), ('E', 'Enke'), ('S', 'Skilt')], max_length=1)),
                ('spouse_id', models.IntegerField(blank=True, default=0)),
                ('spouse_name', models.CharField(blank=True, max_length=255)),
                ('married_date', models.DateField(blank=True, null=True)),
                ('married_place', models.CharField(blank=True, max_length=40)),
                ('death_place', models.CharField(blank=True, max_length=40)),
                ('member_status', models.CharField(choices=[('n', 'New entry - not archived'), ('B', 'Menighetsbarn'), ('M', 'Medlem'), ('U', 'Utmeldt'), ('O', 'Overf??rt til annen menighet')], max_length=1)),
                ('member_since', models.DateField(blank=True, null=True)),
                ('transferred_from', models.CharField(blank=True, max_length=40)),
                ('transferred_from_date', models.DateField(blank=True, null=True)),
                ('transferred_to', models.CharField(blank=True, max_length=40)),
                ('transferred_to_date', models.DateField(blank=True, null=True)),
                ('revoked_membership', models.DateField(blank=True, null=True)),
                ('card_index', models.CharField(max_length=16, null=True)),
                ('card_index_prev', models.CharField(max_length=16)),
                ('notes', models.CharField(blank=True, max_length=2000)),
                ('registered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.country')),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rs_status', models.CharField(choices=[('U', 'Ugift'), ('G', 'Gift'), ('E', 'Enke'), ('S', 'Skilt')], default='G', max_length=1)),
                ('rs_description', models.CharField(max_length=2000)),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userlist.members')),
            ],
        ),
        migrations.CreateModel(
            name='MemberStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ms_status', models.CharField(choices=[('n', 'New entry - not archived'), ('B', 'Menighetsbarn'), ('M', 'Medlem'), ('U', 'Utmeldt'), ('O', 'Overf??rt til annen menighet')], max_length=1, null=True)),
                ('ms_description', models.CharField(max_length=2000)),
                ('ms_is_member', models.BooleanField(default=False)),
                ('membership_since', models.DateField(blank=True, null=True)),
                ('ms_revoked', models.BooleanField(default=False)),
                ('ms_moved', models.BooleanField(default=False)),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userlist.members')),
            ],
        ),
        migrations.CreateModel(
            name='Comitee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comitee_name', models.CharField(max_length=255)),
                ('comitee_description', models.CharField(max_length=2000)),
                ('comitee_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.members')),
            ],
        ),
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=255, unique=True)),
                ('activity_description', models.CharField(max_length=2000)),
                ('activity_leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.members')),
            ],
        ),
        migrations.CreateModel(
            name='MemberComitees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_since', models.DateField(blank=True, null=True)),
                ('comitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.comitee')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.members')),
            ],
            options={
                'unique_together': {('member', 'comitee')},
            },
        ),
        migrations.CreateModel(
            name='MemberActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_since', models.DateField(blank=True, null=True)),
                ('activity', models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='userlist.activities')),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userlist.members')),
            ],
            options={
                'unique_together': {('member', 'activity')},
            },
        ),
    ]
