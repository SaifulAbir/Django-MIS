from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from datetime import datetime
from .models import School,HeadmasterProfile
from accounts.models import User

class HeadmasterResource(resources.ModelResource):
    user =fields.Field(
        column_name='Headmaster Name',
        attribute='user',
        widget=ForeignKeyWidget(User, 'first_name'))

    mobile= Field(attribute='mobile', column_name='Mobile Number')

    school= fields.Field(
        column_name='School Name',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name'))
    #joining_date= Field(attribute='joining_date', column_name='Joining Date')
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

    def dehydrate_joining_date(self,headmaster):
        date_string = str(headmaster.joining_date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')




    class Meta:
        model = HeadmasterProfile
        export_order = ('user','mobile','school','division','district','upazila','union')
        fields = ('user','mobile','school')

