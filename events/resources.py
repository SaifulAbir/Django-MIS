from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from datetime import datetime
from .models import Event


class EventResource(resources.ModelResource):
    class Meta:
        model = Event
        fields = ('title','start_date','end_date')

