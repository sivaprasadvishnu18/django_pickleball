from django.contrib import admin
from .models import Member, Team, Tournament, Tournament_Win

# Register your models here.
admin.site.register(Member)
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Tournament_Win)