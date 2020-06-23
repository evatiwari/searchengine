from .models import Result
def handle_uploaded_file(f):  
    server_path='D:/Documents/Server/'
    result=Result.objects.create(title=f.name,summary='',destination=server_path+f.name)
    result.save()
    with open(server_path+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  