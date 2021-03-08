from django.db import models
from django.utils import timezone


class Countrie(models.Model):
    country_code = models.CharField(max_length=5, null=False, primary_key=True)
    country_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.country_code


class Member(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    RELATION = (
        ('U', 'Ugift'),
        ('G', 'Gift'),
        ('E', 'Enke'),
        ('S', 'Skilt'),
    )
    STATUS = (
        ('n', 'New entry - not archived'),
        ('B', 'Menighetsbarn'),
        ('M', 'Medlem'),
        ('U', 'Utmeldt'),
        ('O', 'Overført til annen menighet'),
    )

    #id = models.IntegerField(unique=True, primary_key=True, auto_created=True)
    last_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=False)
    mid_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    postal_place = models.CharField(max_length=255)
    country_code = models.ForeignKey(Countrie, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255, blank=True)
    phone_home = models.CharField(max_length=20, blank=True)
    phone_work = models.CharField(max_length=20, blank=True)
    phone_cell = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER)
    born = models.DateField()
    birthplace = models.CharField(max_length=40)
    baptised = models.DateField(blank=True, null=True)
    baptised_place = models.CharField(max_length=40, blank=True)
    confirmation = models.DateField(blank=True, null=True)
    confirmation_place = models.CharField(max_length=40, blank=True)
    confirmation_hnr = models.CharField(max_length=16, blank=True)
    father_id = models.IntegerField(default=0, blank=True)
    father = models.TextField(blank=True if father_id else False)
    mother_id = models.IntegerField(default=0, blank=True)
    mother = models.TextField(blank=True if mother_id else False)
    relation_status = models.CharField(max_length=1, choices=RELATION)
    spouse_id = models.IntegerField(default=0, blank=True)
    spouse_name = models.CharField(max_length=255, blank=True)
    married_date = models.DateField(blank=True, null=True)
    married_place = models.CharField(max_length=40, blank=True)
    death_place = models.CharField(max_length=40, blank=True)
    member_status = models.CharField(max_length=1, null=False, choices=STATUS)
    member_since = models.DateField(blank=True, null=True)
    transferred_from = models.CharField(max_length=40, blank=True)
    transferred_from_date = models.DateField(blank=True, null=True)
    transferred_to = models.CharField(max_length=40, blank=True)
    transferred_to_date = models.DateField(blank=True, null=True)
    revoked_membership = models.DateField(blank=True, null=True)
    card_index = models.CharField(max_length=16, null=True)
    card_index_prev = models.CharField(max_length=16)
    notes = models.CharField(max_length=2000, blank=True)
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '(' + str(self.id) + ') ' + str(self.last_name)


class RelationshipStatuse(models.Model):
    member = models.OneToOneField(Member, default=1, on_delete=models.CASCADE)
    rs_status = models.CharField(max_length=1, default='G', choices=Member.RELATION)
    rs_description = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.member) + ' ' + str(self.rs_status)


class Activitie(models.Model):
    activity_name = models.CharField(max_length=255, unique=True)
    activity_description = models.CharField(max_length=2000)
    activity_leader = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity_name


class Comitee(models.Model):
    # com_id = models.SmallIntegerField(primary_key=True, auto_created=True, unique=True)
    comitee_name = models.CharField(max_length=255)
    comitee_description = models.CharField(max_length=2000)
    comitee_leader = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.comitee_name


class MemberStatuse(models.Model):
    member = models.OneToOneField(Member, default=1,  on_delete=models.CASCADE)
    ms_status = models.CharField(max_length=1, null=True, choices=Member.STATUS)
    ms_description = models.CharField(max_length=2000, null=False)
    ms_is_member = models.BooleanField(default=False)
    membership_since = models.DateField(null=True, blank=True)
    ms_revoked = models.BooleanField(default=False)
    ms_moved = models.BooleanField(default=False)


class MemberActivitie(models.Model):
    member = models.ForeignKey(Member, default=1, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activitie, default=6, on_delete=models.CASCADE)
    member_since = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = [['member', 'activity']]


class MemberComitee(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    comitee = models.ForeignKey(Comitee, on_delete=models.CASCADE)
    member_since = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = [['member', 'comitee']]

