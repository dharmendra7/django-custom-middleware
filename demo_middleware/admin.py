from django.contrib import admin
from .models import Newstats

from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

import json
# Register your models here.

# admin.site.register(Newstats)

@admin.register(Newstats)
class NewStatsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        
        stat_data = (
            Newstats.objects.annotate().values("win","mac","iph","android","oth")
        )

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data" : as_json}

        return super().changelist_view(request, extra_context=extra_context)