from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from datetime import datetime
from districts.models import District
from division.models import Division
from topics.models import Topics
from unions.models import Union
from upazillas.models import Upazilla
from .models import School, ClubMeetings


class ClubMeetingResource(resources.ModelResource):
    class_room = Field(attribute='class_room', column_name='Class Room')

    division = fields.Field(
        column_name='Division',
        attribute='division',
        widget=ForeignKeyWidget(Division, 'name'))

    district = fields.Field(
        column_name='District',
        attribute='district',
        widget=ForeignKeyWidget(District, 'name'))

    school = fields.Field(
            column_name='School',
            attribute='school',
            widget=ForeignKeyWidget(School, 'name'))
    #club_establishment_date = fields.Field(column_name='Establishment Date')

    topics = fields.Field(column_name='Topics',
            attribute='topic',widget=ManyToManyWidget(Topics, 'name'))

    def dehydrate_date(self, ClubMeetings):
        date_string = str(ClubMeetings.date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')


    class Meta:
        model = ClubMeetings

        fields = ("date", "class_room", "school",)