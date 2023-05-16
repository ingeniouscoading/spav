from import_export import resources
from .models import Noticeboard

class NoticeResource(resources.ModelResource):
    class Meta:
        model = Noticeboard
        fields = ('notice_title', 'notice_link', 'notice_uploaded_by', 'notice_created_at', 'notice_updated_at')