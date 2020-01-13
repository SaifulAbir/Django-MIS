from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from datetime import datetime
from districts.models import District
from division.models import Division
from unions.models import Union
from upazillas.models import Upazilla
from .models import School

class SchoolResource(resources.ModelResource):
    school_id = Field(attribute='school_id', column_name='EIIN')
    name = Field(attribute='name', column_name='School Name')

    division = fields.Field(
        column_name='Division',
        attribute='division',
        widget=ForeignKeyWidget(Division, 'name'))

    district = fields.Field(
        column_name='District',
        attribute='district',
        widget=ForeignKeyWidget(District, 'name'))

    upazilla = fields.Field(
        column_name='Upazilla',
        attribute='upazilla',
        widget=ForeignKeyWidget(Upazilla, 'name'))

    union = fields.Field(
            column_name='Union',
            attribute='union',
            widget=ForeignKeyWidget(Union, 'name'))

    address = fields.Field(column_name= 'Address')

    class Meta:
        model = School

        fields = ('name','school_id','division','district','upazilla','union','address')

