from django.shortcuts import render
from django.http import HttpResponse
from .models import Result
from .forms import UploadForm
from .functions import handle_uploaded_file
# Create your views here.
def home(request):
    if request.method=='POST':
        upload=UploadForm(request.POST,request.FILES)
        if upload.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File sent to summarizer")
    else:
        upload=UploadForm()
        return render(request,'home.html',{'form':upload})

def search(request):
    search=request
    print(search)
    result=Result.objects.filter(title__contains=search) #.filter(summary__contains=search)
    print(request)
    return render(request,'search.html',{'result':result})
