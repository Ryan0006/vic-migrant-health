from wsgiref.util import FileWrapper
from django.http import HttpResponse

def cert(request):
    filename = "/home/jerrychen0006/IEproject/.well-known/pki-validation/E76D3A577E68F6C252934761B1F88088.txt"
    wrapper = FileWrapper(open(filename))
    return HttpResponse(wrapper, content_type='text/plain')
