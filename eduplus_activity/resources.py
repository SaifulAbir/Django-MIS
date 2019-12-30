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

    def dehydrate_date(self, EduPlusActivity):
        date_string = str(EduPlusActivity.date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')

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
    #club_establishment_date = fields.Field(column_name='Establishment Date')

    topic = fields.Field(column_name='Topics',
            attribute='topics', widget=ManyToManyWidget(EduplusTopics, ',', 'name'))
    attendance = fields.Field(column_name='Attendance',
                         attribute='attendance', widget=ManyToManyWidget(User, ',', 'first_name'))




    class Meta:
        model = EduPlusActivity

        fields = ('date', 'school', 'attendance', 'topics', 'description')
