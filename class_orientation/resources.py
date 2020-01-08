from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from datetime import datetime
from districts.models import District
from division.models import Division
from topics.models import Topics
from unions.models import Union
from upazillas.models import Upazilla
from .models import School, PeerEducation


class PeerEducationResource(resources.ModelResource):
    def dehydrate_created_date(self, PeerEducation):
        date_string = str(PeerEducation.created_date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')

    created_date = fields.Field(column_name='Date')

    topic = fields.Field(column_name='Topics',
                          attribute='topic', widget=ManyToManyWidget(Topics, ',', 'name'))

    place = fields.Field(column_name='Place', attribute='get_place_display')

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

    upazilla = fields.Field(
        column_name='Upazila',
        attribute='school',
        widget=ForeignKeyWidget(School, 'upazilla'))

    union = fields.Field(
        column_name='Union',
        attribute='school',
        widget=ForeignKeyWidget(School, 'union'))


    class Meta:
        model = PeerEducation

        fields = ('created_date', 'place', 'school' 'topic')
        export_order = ('created_date', 'topic', 'place', "school", "division", 'district', 'upazilla', 'union')