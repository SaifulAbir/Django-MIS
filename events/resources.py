from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from datetime import datetime
from .models import Event


class EventResource(resources.ModelResource):
    title = fields.Field(column_name='Title', attribute='title')
    start_date = fields.Field(column_name='Start Date', attribute='start_date', widget=DateTimeWidget(format='%d-%m-%Y'))
    end_date = fields.Field(column_name='End Date', attribute='end_date',
                              widget=DateTimeWidget(format='%d-%m-%Y'))

    class Meta:
        model = Event
        export_order = ('title', 'start_date', 'end_date')
        fields = ('title','start_date','end_date')

