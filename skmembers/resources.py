from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from datetime import datetime
from .models import School,SkMemberProfile
from accounts.models import User

class SkmemberResource(resources.ModelResource):
    name = Field(attribute='name', column_name='Sk Member Name',)
    mobile= Field(attribute='mobile', column_name='Mobile Number')


    school= fields.Field(
        column_name='School Name',
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


    class Meta:
        model = SkMemberProfile

        fields = ('user','mobile','school')

