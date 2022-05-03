from django.contrib import admin
from Session_Phases.models import *

# Register your models here.

admin.site.register(Session)
admin.site.register(Phase)

admin.site.register(Cog_Group)

admin.site.register(Facilitator)
admin.site.register(Participant)