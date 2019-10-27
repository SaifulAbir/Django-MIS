from import_export.fields import Field
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget
from datetime import datetime
from .models import School,SkLeaderProfile
from accounts.models import User

class SkleaderResource(resources.ModelResource):
    user =fields.Field(
        column_name='SK Leader Name',
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

    def dehydrate_joining_date(self,skleader):
        date_string = str(skleader.joining_date)
        if date_string :
            return datetime.strptime(date_string, '%Y-%m-%d').strftime('%d-%m-%Y')




    class Meta:
        model = SkLeaderProfile

        fields = ('user','mobile','student_class','roll','school','joining_date')

