from django.shortcuts import render
from django.http import HttpResponse
from import_export.admin import ExportMixin
from .resources import NoticeResource
from .models import Noticeboard
# Create your views here.

noticeboard = Noticeboard.objects.all()

context = {
    'noticeboard': noticeboard
}

def index(request):
    return render(request, 'index.html')

def noticeboard(request):
    return render(request, 'noticeboard.html', context)

def export_notices_csv(request):
    resource = NoticeResource()
    dataset = resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="notices.csv"'
    return response