from django.shortcuts import render
from django.http import HttpResponse
from app_00.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request): # "request" boleh noleh diubah, asalkan sama dengan ....
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': Webpages_list}
    return render(request, 'index.html', context=date_dict)

