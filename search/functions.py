from .models import Result
from .extract import do_summary
def handle_uploaded_file(f):  
    server_path='D:/Documents/Server/'
    with open(server_path+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    print(server_path+f.name)
    summary=do_summary(server_path+f.name)
    print(summary)
    result=Result.objects.create(title=f.name,summary=summary,destination=server_path+f.name)
    result.save()
    