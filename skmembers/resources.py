from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from datetime import datetime
from .models import School,SkMemberProfile
from accounts.models import User

class SkmemberResource(resources.ModelResource):
    user =fields.Field(
        column_name='Sk Member Name',
        attribute='user',
        widget=ForeignKeyWidget(User, 'first_name'))

    mobile= Field(attribute='mobile', column_name='Mobile Number')
    student_class= Field(attribute='student_class', column_name='Class')
    roll= Field(attribute='roll', column_name='Roll')


    school= fields.Field(
        column_name='School Name',
        attribute='school',
        widget=ForeignKeyWidget(School, 'name'))

    joining_date= Field(attribute='joining_date', column_name='Joining Date')

    def dehydrate_joining_date(self,skmember):
        date_string = str(skmember.joining_date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')




    class Meta:
        model = SkMemberProfile

        fields = ('user','mobile','student_class','roll','school','joining_date')

