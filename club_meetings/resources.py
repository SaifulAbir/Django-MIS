
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
from .models import School, ClubMeetings


class ClubMeetingResource(resources.ModelResource):

    def dehydrate_date(self, ClubMeetings):
        date_string = str(ClubMeetings.date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')

    date = fields.Field(column_name='Date')

    topics = fields.Field(column_name='Topics',
                          attribute='topics', widget=ManyToManyWidget(Topics, ',', 'name'))

    school = fields.Field(
        column_name='School',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name'))

    attendance = fields.Field(column_name='Attendance', attribute='attendance')

    def dehydrate_attendance(self, ClubMeetings):
        return  ClubMeetings.attendance.all().count()

    division = fields.Field(
        column_name='Division',
        attribute='school',
        widget=ForeignKeyWidget(School, 'division'))

    district = fields.Field(
        column_name='District',
        attribute='school',
        widget=ForeignKeyWidget(School, 'district'))

    upazilla = fields.Field(
        column_name='Upazila',
        attribute='school',
        widget=ForeignKeyWidget(School, 'upazilla'))

    union = fields.Field(
        column_name='Union',
        attribute='school',
        widget=ForeignKeyWidget(School, 'union'))

    class Meta:
        model = ClubMeetings
        fields = ("date", 'topics', "school","division", 'district')
        export_order = ('date', 'topics', "school", 'attendance', "division", 'district', 'upazilla')