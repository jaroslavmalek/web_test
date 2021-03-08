from django.contrib import admin
from .models import Member, RelationshipStatuse, Countrie, Activitie, Comitee, MemberStatuse, \
    MemberActivitie, MemberComitee


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'email', 'relation_status', 'member_status')


admin.site.register(Member, UsersAdmin)
admin.site.register(RelationshipStatuse)
admin.site.register(Countrie)
admin.site.register(Activitie)
admin.site.register(Comitee)
admin.site.register(MemberStatuse)
admin.site.register(MemberActivitie)
admin.site.register(MemberComitee)
