from import_export import resources

from districts.models import District
from division.models import Division
from .models import School

class SchoolResource(resources.ModelResource):
    class Meta:
        model = Division