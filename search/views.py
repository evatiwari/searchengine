from django.shortcuts import render
from django.http import HttpResponse
from .models import Result
from .forms import UploadForm
from .functions import handle_uploaded_file
from django.contrib.postgres.search import SearchVector
# Create your views here.
def home(request):
    if request.method=='POST':
        upload=UploadForm(request.POST,request.FILES)
        if upload.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File sent to summarizer")
    else:
        upload=UploadForm()
        return render(request,'home.html',{'uploadform':upload})

def search(request):
    keyword=request.GET.get('search')
    results= Result.objects.annotate(search=SearchVector('title','summary')).filter(search=keyword)
    return render(request, "search.html",{'results':results})