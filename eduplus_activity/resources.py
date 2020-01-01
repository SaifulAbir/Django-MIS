from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from datetime import datetime

from accounts.models import User
from districts.models import District
from division.models import Division
from topics.models import Topics
from unions.models import Union
from upazillas.models import Upazilla
from .models import School, EduPlusActivity, EduplusTopics


class EduPlusActivityResource(resources.ModelResource):

    school = fields.Field(
        column_name='School',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name'))

    division = fields.Field(
        column_name='Division',
        attribute='school',
        widget=ForeignKeyWidget(School, 'division'))

    district = fields.Field(
        column_name='District',
        attribute='school',
        widget=ForeignKeyWidget(School, 'district'))
    upazila = fields.Field(
        column_name='Upazila',
        attribute='school',
        widget=ForeignKeyWidget(School, 'upazilla'))
    union = fields.Field(
        column_name='Union',
        attribute='school',
        widget=ForeignKeyWidget(School, 'union'))
    topic = fields.Field(column_name='Topics',
            attribute='topics', widget=ManyToManyWidget(EduplusTopics, ',', 'name'))
    method = fields.Field(column_name='Method', attribute='method')
    attendance = fields.Field(column_name='Attendance',
                         attribute='attendance', widget=ManyToManyWidget(User, ',', 'first_name'))
    date = fields.Field(column_name='Date',attribute='date')
    description = fields.Field(column_name='Description',attribute='description')







    class Meta:
        model = EduPlusActivity
        exclude = ('id','presence_skleader','image','skleader','topics','method')
        export_order = ('date','topic','method','school', 'attendance','division','district','upazila','union','description' )
        widgets = {
            'date': {'format': '%d.%m.%Y'},
        }

